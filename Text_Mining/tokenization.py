import nltk
import os
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.corpus import stopwords

#Read the base file into a raw text variable
base_file = open(os.getcwd()+ "/notes.txt", 'rt')
raw_text = base_file.read()
base_file.close()


#Extract tokens
token_list = nltk.word_tokenize(raw_text)
print('Token List : ', token_list[:20])
print('\n Total Tokens : ', len(token_list))


#Text Cleansing needs to be done bfore analytics and mL
#1 Formatting and stadardization (eg: dates)
#2 Remove punctuation
#3 Remove abbreviations
#4 Case conversion
#5 Remove elemnts like hashtabs

#Remove Punctuations
#Use the Punkt LIbrary to extract tokens
token_list2= list(filter(lambda token: nltk.tokenize.punkt.PunktToken(token).is_non_punct, token_list))
print('Token List after removing punctuation : ',token_list2[:20])
print('\n Token tokens after removing punctuation : ',len(token_list2))


#Lower case all data:
token_list3=[word.lower() for word in token_list2]
print('Token list after converting to lower case : ', token_list3[:20])
print('\n Total tokens after converting to lower case', len(token_list3))


#remove stop words

token_list4 = list(filter(lambda token: token not in stopwords.words('english'), token_list3))
print('Token list after removing stop words : ', token_list4[:20])
print('\n Total tokens after removing stop words', len(token_list4))


#Steming - a stem is a base part of a word, for example 'combin' is the stem for combine, combining, combined
# Stemming cuts off the affix, so it may not result in a complete word.

#lemmatization
#similar to stemming, but procses a proper root word that belongs to the language
#example: 'combine' is the lemmatized version of combine, combined, and combining
#uses a dictionary to match words to their root word

#n-grams
# is a sequence of n ites in a sample of text
#Bigrams, trigrams, four-grams, and so on

# used for predicting text systems that predict the next text of wods

