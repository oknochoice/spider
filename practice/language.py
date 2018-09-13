from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
from collections import Counter

def cleanSentence(sentence):
    sentence = sentence.split(' ')
    sentence = [word.strip(string.punctuation + string.whitespace) 
        for word in sentence]
    sentence = [word for word in sentence if len(word) > 1 
        or (word.lower() == 'a' or word.lower() == 'i')]
    return sentence


def cleanInput(content):
    content = content.upper()
    content = re.sub('\n', ' ', content)
    content = content.split('.')
    return [cleanSentence(sentence) for sentence in content]

def getNgrams(sentence, n):
    output = []
    for i in range(len(sentence) + 1 - n):
        output.append(sentence[i: i+n])
    return output


content = str(
    urlopen('http://pythonscraping.com/files/inaugurationSpeech.txt').read(), 'utf-8')
content = cleanInput(content)
ngrams = Counter()
for sentence in content:
    newGrams = [' '.join(word) for word in getNgrams(sentence, 2)]
    for gram in newGrams:
        ngrams[gram] += 1
print(ngrams)



