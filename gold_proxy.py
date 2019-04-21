#!/usr/bin/python
"""Reference Modular DRM Proxy Application

Reference proxy built to run via Webapp2 implementation
The Proxy accepts POST requests from CDM players using the 
Widevine License Exchange protol.

This is reference and sample code, not production-ready.

"""

import base64
import json
import logging
import binascii
import sys
import urllib2
import urlparse
import webapp2
import hashlib
from Crypto.Cipher import AES


"""Provider Information"""
# Replace PROVIDER and _KEY and _IV with your provider credentials
_KEY = binascii.a2b_hex("1ae8ccd0e7985cc0b6203a55855a1034afc252980e970ca90e5202689f947ab9")
_IV = binascii.a2b_hex("d58ce954203b7c9a9a9d467f59839249")
PROVIDER = "widevine_test"

# Content Information
CONTENT_ID = base64.b64encode("")

"""License Values"""
LICENSE_SERVER_URL = "https://license.uat.widevine.com/cenc/getlicense"
ALLOWED_TRACK_TYPES = "SD_HD"

"""Setup Console Logging."""
_LOG = logging.getLogger("proxy")
_LOG.setLevel(logging.DEBUG)
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
consoleHandler.setFormatter(formatter)
_LOG.addHandler(consoleHandler)

"""Setup File Logging."""
fileHandler = logging.FileHandler('/var/log/proxy.log')
fileHandler.setLevel(logging.DEBUG)
fileHandler.setFormatter(formatter)
_LOG.addHandler(fileHandler)

class proxyHandler(webapp2.RequestHandler):
  """Proxy Handler for Modular DRM

  Proxies requests between applications using Widevine CDM
   """

  def post(self):
    """Handles HTTP Posts sent to the proxy."""
    self.debug_info = ""
    if self.request.body is None:
      _LOG.debug("Empty Request")
      return None

    # Set CORS correctly
    self.response.headers['Access-Control-Allow-Methods'] = 'POST'
    self.response.headers['Access-Control-Allow-Credentials'] = 'true'
    if self.request.referer is None:
      self.response.headers['Access-Control-Allow-Origin'] = '*'
    else:
      referer = urlparse.urlparse(self.request.referer)
      self.response.headers['Access-Control-Allow-Origin'] = '{0}://{1}'.format(referer.scheme, referer.hostname)

    try:
      if (sys.getsizeof(base64.standard_b64encode(self.request.body)) < 50):
          response = self.sendRequest(self.buildCertificateRequest())
      else:
          response = self.sendRequest(self.buildLicenseServerRequest())
      status_ok, response = self.processLicenseResponse(response)
      if status_ok:
        # Sends response to Player
        self.response.write(response)
      else:
        self.send500(response)
    except TypeError:
      self.send400("Invalid License Request")

  def buildLicenseServerRequest(self):
    """Builds JSON requests to be sent to the license server."""
    message = self.buildLicenseMessage()
    request = base64.standard_b64encode(message)
    signature = self.generateSignature(message)
    license_server_request = json.dumps({"request": request,
                                         "signature": signature,
                                         "signer": PROVIDER})
    return license_server_request
  
  def buildLicenseMessage(self):
    """Build a license request to be sent to Widevine Service."""
    payload = base64.standard_b64encode(self.request.body)
    request = {"payload": payload,
               "content_id": CONTENT_ID,
               "provider": PROVIDER,
               "allowed_track_types": ALLOWED_TRACK_TYPES}
    _LOG.debug("License Request: %s", str(request))
    return json.dumps(request)

  def buildCertificateRequest(self):
    """Builds JSON requests to be sent to the license server."""
    message = self.buildCertificateMessage()
    request = base64.standard_b64encode(message)
    signature = self.generateSignature(message)
    certificate_request = {"request": request,
                           "signature": signature,
                           "signer": PROVIDER}
    return json.dumps(certificate_request)

  def buildCertificateMessage(self):
    """Build a certificate request to be sent to Widevine Service."""
    payload = base64.standard_b64encode(self.request.body)
    request = {"payload": payload}
    _LOG.debug("Certificate Request: %s", str(request))
    return json.dumps(request)

  def sendRequest(self, message_body):
    """Send HTTP request via urllib2"""
    try:
      f = urllib2.urlopen(LICENSE_SERVER_URL + "/" + PROVIDER, message_body)
      return f.read()
    except urllib2.HTTPError:
      self.send500("License Request Failed")

  def generateSignature(self, text_to_sign):
    """Ingest License Request and Encrypt"""
    hashed_text = hashlib.sha1(text_to_sign).digest()
    cipher = AES.new(_KEY, AES.MODE_CBC, _IV)
    padding = binascii.a2b_hex("" if len(hashed_text) % 16 == 0
                                 else (16 -(len(hashed_text) % 16)) * "00")
    aes_msg = cipher.encrypt(hashed_text + padding)
    signature = base64.b64encode(aes_msg)
    return signature

  def processLicenseResponse(self, response):
    """Decode License Response and pass to player"""
    license_response = json.loads(response)
    _LOG.debug("Server response (This is either a license or a certificate): %s", str(license_response)) 
    if license_response["status"] == "OK":
      if license_response.has_key("license"):
        license_decoded = base64.standard_b64decode(license_response["license"])
        return (True, license_decoded)
      else:
         _LOG.debug("PARSE_ONLY request, no 'license' found.")
    else:
      return (False, license_response["status"])

  def get(self):  
    """Handles HTTP Gets sent to the proxy."""
    self.debug_info = None
    self.send400("GET Not Supported")

  def send400(self, text):
    """Send 400 Error Response"""
    self.response.status = 400
    self.response.write(self.response.write(text))

  def send500(self, text):
    """Send 500 Error Response"""
    self.response.status = 500
    self.response.write(self.response.write(text))

app = webapp2.WSGIApplication([('/proxy', proxyHandler),], debug=True)

def main():
  """Setup Portable Web Server."""
  from paste import httpserver
  #from OpenSSL import SSL
  #import ssl

  #context = SSL.Context(SSL.SSLv23_METHOD)
  #context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
  #context.load_cert_chain(certfile="/etc/ssl/jprdigitalott.crt", keyfile = "/etc/ssl/jprdigitalott.key")
  # Assign a SSL key-pair (self-generated or authenticated)
  #context.use_certificate_file('/etc/ssl/jprdigitalott_crt.pem')
  #context.use_privatekey_file('/etc/ssl/jprdigitalott_key.pem')
  httpserver.serve(app, host='0.0.0.0', port='442', ssl_pem="/etc/ssl/jprdigitalott.pem")
  #httpserver.serve(app, host='0.0.0.0', port='8080')
  
  #import ssl
  #import BaseHTTPServer, SimpleHTTPServer
  #httpd = BaseHTTPServer.HTTPServer(('0.0.0.0', 4443), SimpleHTTPServer.SimpleHTTPRequestHandler)
  #httpd.socket = ssl.wrap_socket (httpd.socket, keyfile = "/etc/ssl/jprdigitalott_key.pem", certfile='/etc/ssl/jprdigitalott_crt.pem', server_side=True)
  #httpd.serve_forever()

if __name__ == '__main__':
  main()
