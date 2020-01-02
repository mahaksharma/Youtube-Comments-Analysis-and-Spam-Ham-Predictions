#examples taken from here: http://stackoverflow.com/a/1750187
import csv
with open('onevideo.csv',encoding ="Latin-1") as sourceIn:
    sourceIn = csv.reader(sourceIn)
    headers = next(sourceIn)
    sources = [row for row in sourceIn]
mydoclist = list([row[2]for row in sources])
#numberofunique=len(uniquesources)
#print(numberofunique)
#print (mydoclist)
##mydoclist = ['Julie loves me more than Linda loves me',
##'Jane likes me more than Julie loves me',
##'He likes basketball more than baseball']

#mydoclist = ['sun sky bright', 'sun sun bright']

from collections import Counter
import numpy as np

for doc in mydoclist:
    tf = Counter()
    for word in doc.split():
        tf[word] +=1
    #print (tf.items())

    import string #allows for format()
    
def build_lexicon(corpus):
    lexicon = set()
    for doc in corpus:
        lexicon.update([word for word in doc.split()])
    return lexicon

def tf(term, document):
  return freq(term, document)

def freq(term, document):
  return document.split().count(term)

vocabulary = build_lexicon(mydoclist)

doc_term_matrix = []
print ('Our vocabulary vector is [' + ', '.join(list(vocabulary)) + ']')
for doc in mydoclist:
    print ('The doc is "' + doc + '"')
    tf_vector = [tf(word, doc) for word in vocabulary]
    tf_vector_string = ', '.join(format(freq, 'd') for freq in tf_vector)
    print ('The tf vector for Document %d is [%s]' % ((mydoclist.index(doc)+1), tf_vector_string))
    doc_term_matrix.append(tf_vector)
    
    # here's a test: why did I wrap mydoclist.index(doc)+1 in parens?  it returns an int...
    # try it!  type(mydoclist.index(doc) + 1)

print ('All combined, here is our master document term matrix: ')
#print (doc_term_matrix)

import math

def l2_normalizer(vec):
    denom = np.sum([el**2 for el in vec])
    return [(el / math.sqrt(denom)) for el in vec]

doc_term_matrix_l2 = []
for vec in doc_term_matrix:
    doc_term_matrix_l2.append(l2_normalizer(vec))

print ('A regular old document term matrix: ' )
print( np.matrix(doc_term_matrix))
print ('\nA document term matrix with row-wise L2 norms of 1:')
print (np.matrix(doc_term_matrix_l2))

# if you want to check this math, perform the following:
# from numpy import linalg as la
# la.norm(doc_term_matrix[0])
# la.norm(doc_term_matrix_l2[0])

def numDocsContaining(word, doclist):
    doccount = 0
    for doc in doclist:
        if freq(word, doc) > 0:
            doccount +=1
    return doccount 

def idf(word, doclist):
    n_samples = len(doclist)
    df = numDocsContaining(word, doclist)
    return np.log(n_samples / 1+df)

my_idf_vector = [idf(word, mydoclist) for word in vocabulary]
with open('tfidfanalysis.csv', 'w',encoding='Latin-1',newline='') as f:
    wtr = csv.writer(f)
    
    print ('Our vocabulary vector is [' + ', '.join(list(vocabulary)) + ']')
    print ('The inverse document frequency vector is [' + ', '.join(format(freq, 'f') for freq in my_idf_vector) + ']')
    print(list(vocabulary))

##    for item in list(vocabulary):
##        wtr.writerow([item])
    l2 = [format(freq, 'f') for freq in my_idf_vector]
    print(l2)
    print(list(zip(list(vocabulary),l2)))
    for item in list(zip(list(vocabulary),l2)):
        wtr.writerow([item[0],item[1]])


