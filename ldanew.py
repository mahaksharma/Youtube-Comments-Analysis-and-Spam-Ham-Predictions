from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import csv

tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
en_stop = get_stop_words('en')

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()
import csv

with open('video1.csv', 'r') as f:
  reader = csv.reader(f)
  doc_set = list([ row[0] for row in reader])

print(doc_set)    
# create sample documents
#doc_a = "Brocolli is good to eat. My brother likes to eat good brocolli, but not my mother."
#doc_b = "My mother spends a lot of time driving my brother around to baseball practice."
#doc_c = "Some health experts suggest that driving may cause increased tension and blood pressure."
#doc_d = "I often feel pressure to perform well at school, but my mother never seems to drive my brother to do better."
#doc_e = "Health professionals say that brocolli is good for your health." 

# compile sample documents into a list
#doc_set = [doc_a, doc_b, doc_c, doc_d, doc_e]

# list for tokenized documents in loop
texts = []

# loop through document list

for i in doc_set:
    raw = i.lower() 

    tokens = tokenizer.tokenize(raw)
    print(tokens)

    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]
    print(stopped_tokens)
    # stem tokens
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    print(stemmed_tokens)
    # add tokens to list
    texts.append(stemmed_tokens)

# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)
    
# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

# generate LDA model
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=3, id2word = dictionary, passes=20)
#print(ldamodel.print_topics(num_topics=4, num_words=3))

#for i in range(len(doc_set)):
    #print(ldamodel[corpus[i]]) 	
a=ldamodel.print_topics(num_topics=4, num_words=3)
#print(a)
#print(ldamodel_topics.split())
def unique(a):
    return list(set(a))

with open('video2.csv', 'r') as f:
  reader = csv.reader(f)
  docs_set = list([ row[0] for row in reader])

print(docs_set)    
# create sample documents
#doc_a = "Brocolli is good to eat. My brother likes to eat good brocolli, but not my mother."
#doc_b = "My mother spends a lot of time driving my brother around to baseball practice."
#doc_c = "Some health experts suggest that driving may cause increased tension and blood pressure."
#doc_d = "I often feel pressure to perform well at school, but my mother never seems to drive my brother to do better."
#doc_e = "Health professionals say that brocolli is good for your health." 

# compile sample documents into a list
#doc_set = [doc_a, doc_b, doc_c, doc_d, doc_e]

# list for tokenized documents in loop
textss = []

# loop through document list

for i in docs_set:
    raw = i.lower() 

    tokens = tokenizer.tokenize(raw)
    print(tokens)

    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]
    print(stopped_tokens)
    # stem tokens
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    print(stemmed_tokens)
    # add tokens to list
    texts.append(stemmed_tokens)

# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)
    
# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

# generate LDA model
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=3, id2word = dictionary, passes=20)
#print(ldamodel.print_topics(num_topics=4, num_words=3))

#for i in range(len(doc_set)):
    #print(ldamodel[corpus[i]]) 	
b=ldamodel.print_topics(num_topics=4, num_words=3)
#print(b)
#print(ldamodel_topics.split())
def unique(b):
    return list(set(b))

with open('video3.csv', 'r') as f:
  reader = csv.reader(f)
  docs_set = list([ row[0] for row in reader])

print(docs_set)    
# create sample documents
#doc_a = "Brocolli is good to eat. My brother likes to eat good brocolli, but not my mother."
#doc_b = "My mother spends a lot of time driving my brother around to baseball practice."
#doc_c = "Some health experts suggest that driving may cause increased tension and blood pressure."
#doc_d = "I often feel pressure to perform well at school, but my mother never seems to drive my brother to do better."
#doc_e = "Health professionals say that brocolli is good for your health." 

# compile sample documents into a list
#doc_set = [doc_a, doc_b, doc_c, doc_d, doc_e]

# list for tokenized documents in loop
textss = []

# loop through document list

for i in docs_set:
    raw = i.lower() 

    tokens = tokenizer.tokenize(raw)
    print(tokens)

    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]
    print(stopped_tokens)
    # stem tokens
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    print(stemmed_tokens)
    # add tokens to list
    texts.append(stemmed_tokens)

# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)
    
# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

# generate LDA model
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=3, id2word = dictionary, passes=20)
#print(ldamodel.print_topics(num_topics=4, num_words=3))

#for i in range(len(doc_set)):
    #print(ldamodel[corpus[i]]) 	
c=ldamodel.print_topics(num_topics=4, num_words=3)
print(a)
print(b)
print(c)
#print(ldamodel_topics.split())
def unique(c):
    return list(set(c))
def union(a,b,c):
    return list(set(a)|set(b)|set(c))


print(union(a,b,c))





