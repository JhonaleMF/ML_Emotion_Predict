from utils.variables import *
from nltk.corpus import stopwords

spanish_stopwords = stopwords.words('spanish')

from nltk.stem.snowball import SnowballStemmer

def spanish_stemmer(x):
    stemmer = SnowballStemmer('spanish')
    return " ".join([stemmer.stem(word) for word in x.split()])

def signs_texts(text):
    text = enlaces.sub("", text)
    text = emoji_pattern.sub('', text)
    return signos.sub('', text.lower())

def thebridge(text):    
    return theb.sub('', text.lower())

def remove_stopwords(df):
    return " ".join([word for word in df.split() if word not in spanish_stopwords])