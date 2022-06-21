import nltk
import os
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
nltk.download('punkt')

corpus=PlaintextCorpusReader(os.getcwd(), 'notes.txt')
print(corpus.raw())

print('Files in this corpus : ', corpus.fileids())

#Extract paragraphs from the corpus
paragraphs=corpus.paras()
print('\n Total paragraphs in this corpus : ', len(paragraphs))

#Extract sentences from the corpus
sentences=corpus.sents()
print('\n Total sentences in this corpus : ', len(sentences))
print('\n The first sentence : ', sentences[0])

#Extract words from the corpus
print('\n Words in this corpus : ',corpus.words())


#Find the frequency distribution of the wods in the corpus
course_freq_dist=nltk.FreqDist(corpus.words())

#Print most commenly used words
print('Top 10 words in the corpus : ', course_freq_dist.most_common(10))

#find the distrbution for a specific word
print('\n Distribution for \"is\" : ', course_freq_dist.get('is'))


