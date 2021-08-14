from string import punctuation
from nltk.tokenize.treebank import TreebankWordDetokenizer

import re, nltk

def remove_punct(text):
    text  = "".join([char for char in text if char not in punctuation])
    text = re.sub('[0-9]+', '', text)
    text = re.sub('http\S+', '', text)
    text = re.sub('\S*@\S*\s?', '', text)
    text = re.sub('\s+', ' ', text)
    text = re.sub("\'", "", text)
    text = re.sub(r'http\S+', '', text)
    return text

def tokenization(text):
    text = re.split('\W+', text)
    return text

def remove_stopwords(text):
    stopword = nltk.corpus.stopwords.words('indonesian')
    stopword.extend(['bot'])
    text = [word for word in text if word not in stopword]
    return text

def detokenization(text):
    text = TreebankWordDetokenizer().detokenize(text)
    return text