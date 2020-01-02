import csv
import numpy
import networkx as nx
import matplotlib.pyplot as plt
import nltk
#nltk.download('all')
from nltk.corpus import stopwords

#with open('finalpunc.csv',encoding ="Latin-1") as sourceIn:
#with open('nasciipunc.csv',encoding ="Latin-1") as sourceIn:
with open('finalpunc.csv',encoding ="Latin-1") as sourceIn:

    sourceIn = csv.reader(sourceIn)
    headers = next(sourceIn)
    sources = [row for row in sourceIn]
uniquesources = list(set([row[0] for row in sources]))
id=list(enumerate(uniquesources))
keys = {source:i for i, source in enumerate(uniquesources)}   
links = []
#with open('teststopword.csv', 'w',encoding='Latin-1',newline='') as f:
with open('newstopword.csv', 'w',encoding='Latin-1',newline='') as f:
      wtr = csv.writer(f)
      #operators = set(('a', 'b', 'use'))
      #stop = set(stopwords.words('english'))
      for row in sources:
            word_list = row[2].split()
            filtered_word_list = word_list[:] #make a copy of the word_list
            for word in word_list: # iterate over word_list
                  #print (stopwords.words('english'))
                  if word in stopwords.words('english'):
                        filtered_word_list.remove(word)
                        word_list=filtered_word_list
            
            wtr.writerow([row[0],row[1],' '.join(word_list)])
            #wtr.writerow([word_list])
            
                 # print (filtered_word_list)
            #print (word)
            #if True in row[3]:
            #wtr.writerow([row[0],row[1],row[3],row[2].encode('ascii', errors='ignore')])
            #try:
                  #newrow = [''.join(' ' if c in stop else c for c in entry) for entry in row]
                  #wtr.writerow(newrow)
                  #if row[2].lower().split() not in stop:
                   #     links.append({row[0]: row[1]})
                
        #print (row[3],row[1],row[2])
           # except:
             #     links.append(row[3])
        
        #row[3].to_csv('E:\6th sem\project files/new.csv',index=False)
    #print (count)
G = nx.Graph() #creates a graph
pos = nx.random_layout(G)
sourceNodeId=[] #takes source and target edges
for row in id:
 sourceNodeId.append(row[0])
G.add_nodes_from(sourceNodeId)#creates nodes for the graph.
#print("Total number of video nodes are:", G.number_of_links())
for node in links:
 edges = list(node.items())
 G.add_edge(*edges[0])
nx.draw_networkx(G)
    # if (row[3] == True):
           # print (row[3])
