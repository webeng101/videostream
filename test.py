# from difflib import SequenceMatcher
# import mailchimp
# import requests, json, http.client, urllib.request, urllib.parse, urllib.error, base64, \
#     itertools, re
# import bible_api.biblegateway_api
# from lxml import etree
# from nltk.tokenize import sent_tokenize, word_tokenize
# import nltk
# from collections import defaultdict
import slate
import slate.utils

mylist = ['Kingdom of Saudi Arabia', 'Southern Arabia', 'c', 'd', 'e', 'f', 'g', 'h']

logic = ['AND', 'OR']

Result = []

Book = {'Preface': 'FRT', 'Genesis': 'GEN', 'Exodus': 'EXO', 'Leviticus': 'LEV', 'Numbers': 'NUM', 'Deuteronomy': 'DEU', 'Joshua': 'JOS', 'Judges': 'JDG', 'Ruth': 'RUT', 'The First Book of Samuel': '1SA', 'The Second Book of Samuel': '2SA', 'The First Book of Kings': '1KI', 'The Second Book of Kings': '2KI', 'The First Book of Chronicles': '1CH', 'The Second Book of Chronicles': '2CH', 'Ezra': 'EZR', 'Nehemiah': 'NEH', ' Esther': 'EST', 'Job': 'JOB', 'Psalms': 'PSA', 'Proverbs': 'PRO', ' Ecclesiastes': 'ECC', ' Song of Solomon': 'SNG', 'Isaiah': 'ISA', 'Jeremiah': 'JER', 'Lamentations': 'LAM', 'Ezekiel': 'EZK', ' Daniel': 'DAN', 'Hosea': 'HOS', 'Joel': 'JOL', 'Amos': 'AMO', 'Obadiah': 'OBA', 'Jonah': 'JON', 'Micah': 'MIC', 'Nahum': 'NAM', 'Habakkuk': 'HAB', 'Zephaniah': 'ZEP', 'Haggai': 'HAG', 'Zechariah': 'ZEC', 'Malachi': 'MAL', 'A01-TOB-kjv.sfm The King James Version of the Holy Bible Wednesday, October 14, 2009': 'TOB', 'A02-JDT-kjv.sfm The King James Version of the Holy Bible Wednesday, October 14, 2009': 'JDT', 'A03-ESG-kjv.sfm The King James Version of the Holy Bible Wednesday, October 14, 2009': 'ESG', 'A04-WIS-kjv.sfm The King James Version of the Holy Bible Wednesday, October 14, 2009': 'WIS', 'A05-SIR-kjv.sfm The King James Version of the Holy Bible Wednesday, October 14, 2009': 'SIR', 'A06-BAR-kjv.sfm The King James Version of the Holy Bible Wednesday, October 14, 2009': 'BAR', 'A08-S3Y-kjv.sfm The King James Version of the Holy Bible Wednesday, October 14, 2009': 'S3Y', 'A09-SUS-kjv.sfm The King James Version of the Holy Bible Wednesday, October 14, 2009': 'SUS', 'A10-BEL-kjv.sfm The King James Version of the Holy Bible Wednesday, October 14, 2009': 'BEL', 'A11-1MA-kjv.sfm The King James Version of the Holy Bible Wednesday, October 14, 2009': '1MA', 'A12-2MA-kjv.sfm The King James Version of the Holy Bible Wednesday, October 14, 2009': '2MA', 'A13-1ES-kjv.sfm The King James Version of the Holy Bible Wednesday, October 14, 2009': '1ES', 'A14-MAN-kjv.sfm The King James Version of the Holy Bible Wednesday, October 14, 2009': 'MAN', 'A17-2ES-kjv.sfm The King James Version of the Holy Bible Wednesday, October 14, 2009': '2ES', 'The Gospel According to Matthew': 'MAT', 'The Gospel According to Mark': 'MRK', 'The Gospel According to Luke': 'LUK', 'The Gospel According to John': 'JHN', 'The Acts of the Apostles': 'ACT', 'Paul’s Letter to the Romans': 'ROM', 'Paul’s First Letter to the Corinthians': '1CO', 'Paul’s Second Lettor to the Corinthians': '2CO', 'Paul’s Letter to the Galatians': 'GAL', 'Paul’s Letter to the Ephesians': 'EPH', 'Paul’s Letter to the Philippians': 'PHP', 'Paul’s Letter to the Colossians': 'COL', 'Paul’s First Letter to the Thessalonians': '1TH', 'Paul’s Second Letter to the Thessalonians': '2TH', 'Paul’s First Letter to Timothy': '1TI', 'Paul’s Second Letter to Timothy': '2TI', 'Paul’s Letter to Titus': 'TIT', 'Paul’s Letter to Philemon': 'PHM', 'The Letter to the Hebrews': 'HEB', 'The Letter from James': 'JAS', 'The First Letter from Peter': '1PE', 'The Second Letter from Peter': '2PE', 'John’s First Letter': '1JN', 'John’s Second Letter': '2JN', 'John’s Third Letter': '3JN', 'Jude’s Letter': 'JUD', 'The Revelation to John': 'REV'}


# def logic_combination(terms):
#     """
#     Make logic combination for AND, OR
#     :param terms:
#     :return:
#     """
#     if terms:
#         n = len(terms) - 1
#         l1 = n * ["AND"]
#         result = []
#         for i in range(n):
#             if i == 0:
#                 result.append(tuple(l1))
#                 continue
#             l1[n - i] = 'OR'
#             result += (list(set(list(x for x in itertools.permutations(l1)))))
#         result.append(tuple(n * ["OR"]))
#
#         query_list = []
#         for item in result:
#             query_item = ""
#             for index, term in enumerate(terms):
#                 query_item += term
#                 query_item += " "
#                 query_item += item[index] if index < len(terms) - 1 else ""
#                 query_item += " " if index < len(terms) - 1 else ""
#             query_list.append(query_item)
#
#         print('query list: {}'.format(query_list))
#         return query_list
#
#     return []
#
#
# def API_call_URL(url, targets):
#     alch_call = """http://gateway-a.watsonplatform.net/calls/url/URLGetRankedNamedEntities?outputMode=json&apikey=""" + \
#                 'cd869cbb5f9fc0b44ec8e6194a27db53c3c0491b' + "&url=" + url
#     r = requests.get(alch_call).text
#
#     # Need to catch an exception here for if the API call does not work
#     URL_RESULT = []
#     if 'entities' in json.loads(r):
#         ents = json.loads(r)['entities']
#         print('======================== ents: ==========================={}'.format(ents))
#
#         if len(ents) > 0:
#             for entity in ents:
#                 if entity['type'] != 'Quantity':
#                     for targ in targets:
#                         URL_RESULT.append({'type': entity['type'],
#                                            'text': entity['text'],
#                                            'relevance': float(entity['relevance']),
#                                            'target': targ,
#                                            'url': url})
#     return URL_RESULT
#
#
# def API_call_Search(Keyword_list, final_recursion=False):
#     """
#     Algorithm to search entities from text using Azure API.
#     :param Keyword_list:
#     :param level:
#     :param nullThird:
#     :return:
#     """
#     headers = {'Ocp-Apim-Subscription-Key': '224f54c59f664ac88e653844845f30a0'}
#
#     query_list = logic_combination(Keyword_list)
#     result_url = []  # store URLs from bing Web API Service without duplicated
#     entities = []  # Save entities from IBM watson service
#
#     print('=================== query_list ==================== {}'.format(query_list))
#     # for query in query_list:
#     #     params = urllib.parse.urlencode({
#     #         'q': query,
#     #         'count': '15',
#     #         'offset': '0',
#     #         'mkt': 'en-us',
#     #         'safesearch': 'Moderate',
#     #     })
#     #
#     #     conn = http.client.HTTPSConnection('api.cognitive.microsoft.com')
#     #     conn.request("GET", "/bing/v5.0/search?%s" % params, "{body}", headers)
#     #     response = conn.getresponse()
#     #     # conn.close()
#     #     data = response.read()
#     #     y = json.loads(data.decode('utf8'))['webPages']['value']
#     #     print('==================== Query:================ {}'.format(query))
#     #     count = 0  # Filtering 3 top links.
#     #
#     #     for i in range(len(y)):
#     #         url = 'http' + y[i]['url'].split('=http')[1]
#     #         url = url.split('&p=DevEx')[0]
#     #         url = re.sub('%2f', '/', url)
#     #         url = re.sub('%3a', ':', url)
#     #         # print("================== URL =================  {}".format(url))
#     #         if not url in result_url:
#     #             result_url.append(url)
#     #             if count > 2:
#     #                 break
#     #             __entities = API_call_URL(url, Keyword_list)
#     #             if __entities:
#     #                 entities += __entities
#     #                 count += 1
#     #
#     # print('entities: {}'.format(entities))
#     # unique = {each['text']: each for each in entities}
#     #
#     # print('result: {}'.format(unique))
#     #
#     # return unique
#
#
# def recursiveCall(keyword_list, original_list):
#     """
#     Recursive Call
#     :param keyword_list:
#     :param original_list:
#     :return:
#     """
#     recursion_list = []
#     temp = []
#     for keyword in keyword_list:
#         temp = original_list + [keyword.values()['text']]
#         temp = itertools.combinations(temp, 2)
#         recursion_list += temp
#         temp = itertools.combinations(temp, 3)
#         recursion_list += temp
#     print('recursino_list: {}'.format(recursion_list))
#
#
# def safe_unicode(obj, *args):
#     """ return the unicode representation of obj """
#     try:
#         return str(obj, *args)
#     except UnicodeDecodeError:
#         # obj is byte string
#         ascii_text = str(obj).encode('string_escape')
#         return str(ascii_text)
#
#
# def safe_str(obj):
#     """ return the byte string representation of obj """
#     try:
#         return str(obj)
#     except UnicodeEncodeError:
#         # obj is unicode
#         return str(obj).encode('unicode_escape')
#
#
# def API_call_Ocr(filename):
#     """
#     Algorithm to extract the string from image using Azure API.
#     :return:
#     """
#     result = None
#     lines = []
#     headers = {
#         # Request headers
#         'Content-Type': 'application/json',
#         'Ocp-Apim-Subscription-Key': '1a61f6c4f3164a478717b039d515ca4f',
#     }
#
#     params = urllib.parse.urlencode({
#         # Request parameters
#         'language': 'unk',
#         'detectOrientation ': 'true',
#     })
#
#     body = {'url': 'https://gtrpweb.com/static/ocr/' + filename}
#
#     try:
#         conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
#         conn.request("POST", "/vision/v1.0/ocr?%s" % params, json.dumps(body), headers)
#         response = conn.getresponse()
#         data = response.read().decode('utf8').replace("'", '"')
#         data = json.loads(data)
#         print(data)
#         print('----------------data load--------------------')
#         # result = json.dumps(data, indent=4, sort_keys=True)
#         conn.close()
#         for item in data['regions']:
#             print(item)
#             try:
#                 for item_1 in item['lines']:
#                     words = ""
#                     for item_2 in item_1['words']:
#                         words += item_2["text"] + " "
#                     lines.append(words)
#             except:
#                 continue
#     except Exception as e:
#         print("[Errno {0}]".format(e))
#
#     return lines
#
#
# def API_Concordance(path):
#     """
#     Test the words concordance.
#     :param path:
#     :return:
#     """
#     import nltk.corpus
#     from nltk.text import Text
#     textList = Text(nltk.corpus.gutenberg.words('bible-kjv.txt'))
#     ext = textList.concordance('Esau')
#     print('ext: {}'.format(ext))
#
#
# def stringify_children(node):
#     from lxml.etree import tostring
#     from itertools import chain
#     parts = ([node.text] +
#             list(chain(*([c.text, tostring(c), c.tail] for c in node.getchildren()))) +
#             [node.tail])
#     # filter removes possible Nones in texts and tails
#     return ''.join(filter(None, parts))
#
#
# def search_xml(reference='Genesis 25:26'):
#     """
#     Search strong number based on reference.
#     :param reference:
#     :return:
#     """
#     root = etree.parse('bible_api/eng-kjv_usfx.xml')
#
#     ref_book = reference.split(" ")[0]
#     ref_chapter = reference.split(" ")[1].split(":")[0]
#     ref_verse = reference.split(" ")[1].split(":")[1]
#     print(ref_book, ref_chapter, ref_verse)
#     ref = Book[ref_book] + "." + ref_chapter + "." + ref_verse
#     print('ref: {}'.format(ref))
#     xPath = ".//v[@bcv=" + "'GEN.2.4']"
#     matched_el_list = root.xpath(xPath)
#     print(len(matched_el_list))
#     matched_el = matched_el_list[0]
#     print(matched_el.attrib)  # get attrib
#     print(matched_el.tag)  # get tag
#     print(matched_el.text)  # get text
#     while True:
#         next_ele = matched_el.getnext()  # get next
#         print('text {}'.format(next_ele.text))
#         print('attrib: {}'.format(next_ele.attrib))
#         if next_ele.attrib == {}:
#             print("=========nd")
#             print("".join([x for x in next_ele.itertext()]))
#         if next_ele.tag == "v":
#             break
#         matched_el = next_ele
#
#
# def search_word():
#     root = etree.parse('bible_api/eng-kjv_usfx.xml')
#
#     xPath = ".//w[@s='H4735']"
#     matched_el_list = root.xpath(xPath)
#     print(len(matched_el_list))
#     print(matched_el_list[4].text)
#
#     # for matched_el in matched_el_list:
#     #     if "LORD" in "".join([x for x in matched_el.itertext()]):
#     #         print("".join([x for x in matched_el.itertext()]))
#     #         content = "".join([x for x in matched_el.itertext()])
#     #         while True:
#     #             next_ele = matched_el.getprevious()  # get next
#     #             if next_ele is not None and next_ele.tag == "v":
#     #                 print("v ========\n")
#     #                 print(next_ele.tag)
#     #                 print(next_ele.attrib)
#     #                 break
#     #             matched_el = next_ele
#     #         print(matched_el.attrib)
#     #         if matched_el.attrib == {}:
#     #             print("strong number: {}".format(content.split("=")[1]))
#     #             break
#
#
# def search_greek():
#     root = etree.parse('bible_api/greek_lexicon.xml')
#     xPath = ".//entry/kjv_def"
#
#     matched_ele_list = root.xpath(xPath)
#
#     for item in matched_ele_list:
#         print(item.text)
#         if 'death' in item.text:
#             print("================")
#             print(item.text)
#             print(item.getparent().attrib)
#             break
#
#
# def internal_search():
#     bg_api = bible_api.biblegateway_api
#     # search result in bible getting a dictionary (reference,text)
#     results = bg_api.get_search_result("ESAU")
#     print(results)
#     print(len(results))
#     # print("\n\n****** Result for searching Fruit Spirit ********")
#     # for (reference, text) in results.items():
#     #     print("Reference: " + reference)
#     #     print("Text: " + text)
#     #     search_xml(reference=reference)
#     # # get verse of the day
#     # result = bg_api.getVotd()
#     # print("\n\n****** Verse of the Day ********")
#     # print("Reference :" + result['reference'])
#     # print("Version :" + result['version'])
#     # print(result['text'])
#
#
# def search_term(terms=["LORD"]):
#     root = etree.parse('bible_api/eng-kjv_usfx.xml')
#     xPath = ".//v"
#     matched_el_list = root.xpath(xPath)
#     print("terms: {}".format("LORD"))
#
#     for matched_el in matched_el_list:
#         content = ""
#         strong_numbers = []
#         temp_matched_el = matched_el
#
#         # if terms[0] in content:
#         while True:
#             next_ele = temp_matched_el.getnext()
#             # get next
#             if next_ele is None:
#                 break
#             elif "w" in next_ele.tag:
#                 content += " ".join([x for x in next_ele.itertext()])
#                 content += " "
#                 strong_numbers.append(next_ele.attrib['s'])
#             if next_ele.tag == "v" or next_ele.tag == "ve":
#                 break
#
#             temp_matched_el = next_ele
#
#         # if terms[0] in content or terms[0] in strong_numbers:
#         #     result[str(matched_el.attrib['bcv'])] = content
#     print("complete search_term")
#
# def add_mailchimp():
#     API_KEY = '5e7b7fa236430cae3cfbe998c766576d-us3'
#     LIST_ID = '0439147cc4'
#     api = mailchimp.Mailchimp(API_KEY)
#     api.lists.subscribe(LIST_ID, {'email': "test9@mail.com"}, double_optin=False, update_existing=True)
#
#
# def merge_terms(ref):
#     print(ref.split(".")[0])
#     print(Book[ref.split(".")[0]])
#     a = ref.replace(ref.split(".")[0], Book[ref.split(".")[0]])
#     ref.replace("Genesis", "GEN")
#     print(a)
#
#
# def get_relatvie(text):
#     relatived = []
#     sentences = sent_tokenize(text)
#     tokenized_sentences = [word_tokenize(sentence) for sentence in sentences]
#     tagged_sentences = [nltk.tag.pos_tag(sentence) for sentence in tokenized_sentences]
#     grammar = r"""
#             NBAR:
#                 {<NN.*|JJ>*<NN.*>}  # Nouns and Adjectives, terminated with Nouns
#
#             NP:
#                 {<NBAR><IN><NBAR>}  # Above, connected with in/of/etc...
#         """
#
#     cp = nltk.RegexpParser(grammar)
#     result = cp.parse(tagged_sentences[0])
#     for item in result:
#         if isinstance(item, nltk.Tree):
#             print("tree: {}".format(item.leaves()))
#             relatived.append(" ".join(item[0] for item in item.leaves()))
#         elif item[1] == "NBAR" or item[1] == "NP":
#             print("item 0: {}".format(item[0]))
#             print("item 1: {}".format(item[1]))
#             relatived.append(item[0])
#     print(relatived)
#
#
# def longestSubstringFinder(string1, string2):
#     answer = []
#     tokenized_word1 = word_tokenize(string1)
#     tokenized_word2 = word_tokenize(string2)
#     compared = list(set(tokenized_word1) & set(tokenized_word2))
#     for word in compared:
#         if nltk.tag.pos_tag([word])[0][1] in ['JJ', 'NN', 'NNS', 'NP', 'NNP']:
#             answer.append(word)
#     return answer
#
#
# def get_common_substring(temp_terms, length):
#     """
#     Get the English Translated word from strong number.
#     :return: {strong number: word list}
#     """
#     english_translated_words = []
#     temp_result = []
#     if len(temp_terms) > 1:
#         temp_result = []
#         for x, y in itertools.combinations(temp_terms, 2):
#             english_translated_words += longestSubstringFinder(x, y)
#
#         d = defaultdict(int)
#         for i in english_translated_words:
#             d[i] += 1
#         descending = sorted(d.items(), key=lambda x: x[1], reverse=True)
#         for text, count in descending:
#             if count > length/2:
#                 temp_result.append(text.split(" ")[-1])
#
#     result = list(set(temp_result))[0:2]
#     print('result: {}'.format(result))
#     return result
#
#
# def search_text(text):
#     sent_tokenize_list = sent_tokenize(text=text)
#     print(len(sent_tokenize_list))
#     print(sent_tokenize_list)
#     for sentence in sent_tokenize_list:
#         word_tokenize_list = word_tokenize(text=sentence)
#         if "giants" in word_tokenize_list:
#             print(sentence)
#
#
# def recursion(term):
#     """
#     Recursion Function.
#     :param term:
#     :return:
#     """
#     original_terms_list = []
#     strong_numbers_list = []
#     references_list = []
#
#     def search_term_by_word(word):
#         """
#         Search terms in xml file
#         :param terms:
#         :return: {reference: data, word: [strong number list]}
#         """
#         reference_item = {word: [],
#                           'reference': {}}
#         original_terms_list.append(word)  # add word to original terms list.
#
#         root = etree.parse('bible_api/eng-kjv_usfx.xml')
#         xPath = ".//v"
#         matched_el_list = root.xpath(xPath)
#         print("term: {}".format(word))
#
#         for matched_el in matched_el_list:
#             content = ""
#             temp_matched_el = matched_el
#
#             # if term in content:
#             while True:
#                 next_ele = temp_matched_el.getnext()
#                 # get next
#                 if next_ele is None:
#                     break
#                 elif "w" in next_ele.tag:
#                     subcontent = " ".join([x for x in next_ele.itertext()])
#                     content += subcontent
#                     content += " "
#
#                     # Search strong's number for special word.
#                     if word in subcontent:  # search only by "w" tag.
#                         if "s" in next_ele.attrib:  # check if "s" key exists in attribute.
#                             reference_item[word].append(next_ele.attrib["s"])
#
#                         elif next_ele.attrib == {}:
#                             try:
#                                 strong_number = re.search(r'strong=\'(\w\d+)\'', content)
#                                 reference_item[word].append(strong_number[1])
#                             except Exception as e:
#                                 pass
#
#                 if next_ele.tag == "v" or next_ele.tag == "ve":
#                     break
#                 temp_matched_el = next_ele
#
#             if word in content:
#                 reference_item['reference'][str(matched_el.attrib['bcv'])] = content
#
#         reference_item[word] = list(set(reference_item[word]) - set(strong_numbers_list))[0:2]
#         save_to_reference(reference_item=reference_item, word=word)
#         print('reference item: {}'.format(reference_item))
#         print("===========complete search_term_by_word============")
#
#         return reference_item
#
#     def save_to_reference(reference_item, word):
#         """
#         Save reference item to reference list
#         :param reference_item:
#         :return:
#         """
#         for strong_num in reference_item[word]:
#             if len(reference_item['reference']) > 0:
#                 for (reference, text) in reference_item['reference'].items():
#                     references_list.append({"reference": reference,
#                                             "text": text,
#                                             "term": word,
#                                             "strong_number": strong_num})
#
#     def search_term_by_strong(strong_number):
#         """
#         Search term by strong's number
#         {term: [word list]}
#         :param term:
#         :return:
#         """
#
#         temp_terms = []
#         strong_numbers_list.append(strong_number)  # add strong number to list.
#
#         root = etree.parse('bible_api/eng-kjv_usfx.xml')
#         xPath = ".//w[@s='" + strong_number + "']"
#         matched_el_list = root.xpath(xPath)
#         for matched_el in matched_el_list:
#             temp_terms.append(matched_el.text)
#
#         temp_terms_list = get_common_substring(temp_terms=temp_terms, length=len(temp_terms))
#         print("words_list: {}".format(list(set(temp_terms_list) - set(original_terms_list))))
#         return list(set(temp_terms_list) - set(original_terms_list))  # return words_list
#
#     def recursion_term(term):
#
#         if bool(re.match(r'[A-Z]\d+', term)):
#             words_list = search_term_by_strong(strong_number=term)
#             if len(words_list) == 0:
#                 return
#             for word in words_list[:2]:
#                 recursion_term(term=word)
#         else:
#             reference_item = search_term_by_word(word=term)
#             if len(reference_item[term]) == 0:
#                 return
#             for strong_number in reference_item[term][:3]:
#                 print('strong number: {}'.format(strong_number))
#                 recursion_term(term=strong_number)
#
#     recursion_term(term=term)
#     print('reference_list: {}'.format(references_list))
#     return references_list
#
#
# def search_term_by_word(word):
#     """
#     Search terms in xml file
#     :param terms:
#     :return: {reference: data, word: [strong number list]}
#     """
#     reference_item = {word: [],
#                       'reference': {}}
#     # original_terms_list.append(word)  # add word to original terms list.
#     #
#     root = etree.parse('bible_api/eng-kjv_usfx.xml')
#     xPath = ".//v"
#     matched_el_list = root.xpath(xPath)
#     print("term: {}".format(word))
#
#     for matched_el in matched_el_list:
#         content = ""
#         temp_matched_el = matched_el
#
#         # if term in content:
#         while True:
#             next_ele = temp_matched_el.getnext()
#             # get next
#             if next_ele is None:
#                 break
#             elif "w" in next_ele.tag:
#                 subcontent = " ".join([x for x in next_ele.itertext()])
#                 content += subcontent
#                 content += " "
#
#                 # Search strong's number for special word.
#                 if word in subcontent:  # search only by "w" tag.
#                     if "s" in next_ele.attrib:  # check if "s" key exists in attribute.
#                         reference_item[word].append(next_ele.attrib["s"])
#
#                     elif next_ele.attrib == {}:
#                         try:
#                             strong_number = re.search(r'strong=\'(\w\d+)\'', content)
#                             reference_item[word].append(strong_number[1])
#                         except Exception as e:
#                             pass
#
#             if next_ele.tag == "v" or next_ele.tag == "ve":
#                 break
#             temp_matched_el = next_ele
#
#         if word in content:
#             reference_item['reference'][str(matched_el.attrib['bcv'])] = content
#
#     # reference_item[word] = list(set(reference_item[word]) - set(strong_numbers_list))[0:2]
#     # save_to_reference(reference_item=reference_item, word=word)
#     print('reference item: {}'.format(reference_item))
#     print("===========complete search_term_by_word============")
#
#
#     # return reference_item
#
#
# def similar(target_list):
#     duplicated = {}
#     result = target_list
#     for x, y in itertools.combinations(target_list, 2):
#         if SequenceMatcher(None, x, y).ratio() >= 0.7:
#             if x not in duplicated.keys():
#                 duplicated[x] = [y]
#             else:
#                 duplicated[x].append(y)
#     for key, value in duplicated.items():
#         result = list(set(result)- set(value))
#     print(result)
#     # return list(set(duplicated.keys()) - set(original_list))[:2]
#
# def test():
#     return "test", "path"


if __name__ == '__main__':
    # keyword_list = API_call_Search(mylist)
    # recursiveCall(keyword_list, mylist)
    # logic_combination(mylist)
    # API_Concordance(None)
    # internal_search()
    # search_xml()
    # search_greek()
    # find_associated()
    # search_word()
    # merge_terms("Genesis.6.5")
    # if re.match(r'[A-Z]\d+', "2634"):
    #     print("True")
    # get_relatvie("There were giants in the earth in those days; "
    #              "and also after that, when the sons of God came in unto the daughters of men, "
    #              "and they bare children to them, the same became mighty men which were of old, men of renown.")
    # search_term_by_strong("giants")
    # search_term_by_word("giants")
    # search_text("There were giants in the earth in those days. "
    #              "and also after that, when the sons of God came in unto the daughters of men. "
    #              "and they bare children to them, the same became mighty men which were of old, men of renown.")
    # print(word_tokenize("the river"))
    # recursion(term="giants")
    # search_term_by_strong('H7497')
    # search_term_by_word('Rephaim')
    # temp_terms = ["There were the giants", "of the giants", "the giants", "giant", "the giant"]
    # get_common_substring(temp_terms=temp_terms)
    # longestSubstringFinder(temp_terms[0], temp_terms[1])
    # print(nltk.tag.pos_tag(['think']))
    # found = re.search(r'strong=\'(\w\d+)\'', "<nd>LORD</nd>|strong='H3068'</w>;")
    # print(found[1])
    # print(sent_tokenize("His prophecy became true in 68 C.E. when Nero committed suicide and Vespasian becameCeasar. As a result, Josephus was freed; he moved to Roman and became a Roman citizen,taking the Vespasian family name Flavius. Vespasian commissioned Josephus to write a historyof the war, which he finished in 78 C.E., the Jewish War. His second major work, the Antiquitiesof the Jews, was completed in 93 C.E. He wrote Against Apion in about 96-100 C.E. and TheLife of Josephus, his autobiography, about 100. He died shortly after."))
    with open('D_1-2_Maccabees_pp_517-567_245.pdf') as f:
        doc = slate.PDF(f)
        print(doc)