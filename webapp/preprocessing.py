# function to remove 'READ MORE'
def read_more(data):
    data = data.replace('READ MORE','')
    return data


# function to normalize data
def normalization(data):
    return data.lower()


# function to replace emojis with its meaning text
import emoji
def remove_emoji(data):
    x=''
    for i in data:
        if emoji.is_emoji(i):
            x=x+' '+ emoji.demojize(i)
        else:
            x=x+i
    return x.strip()


# function to remove punctuation
from string import punctuation
def remove_punctuation(data):
    return ''.join([i for i in data if i not in punctuation])


# function to remove digits
def remove_digit(data):
    x=''
    for i in data:
        if i.isdigit() == False:
            x = x + i
    return x


# function to autocorrect text spellings
from autocorrect import Speller
def auto_correction(data):
    spell=Speller(lang='en')
    return spell(data)


# function to fixing contraction
import contractions
def contraction_fixing(data):
    return contractions.fix(data)


# function to remove stopwords
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

swl=stopwords.words('english')
swl.remove('no')
swl.remove('not')
swl.remove('nor')

def remove_stopwords(data):
    return ' '.join([i for i in data.split() if i.lower() not in swl])


# funtion to fixing accented text
from unidecode import unidecode
def accented_fixing(data):
    return unidecode(data)


# function to stemming the text
from nltk.stem import PorterStemmer
def stemming(data):
    stemmer = PorterStemmer()

    x=''
    for i in data.split():
        x = x +' ' + stemmer.stem(i)
    return x.strip()


# function to tokenize the text
nltk.download('punkt')
def tokenization(data):
    tokens = nltk.word_tokenize(data)
    return tokens
print('preprocessing completed')