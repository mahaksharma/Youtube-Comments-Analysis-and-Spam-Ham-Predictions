import csv
import numpy
import networkx as nx
import matplotlib.pyplot as plt

with open('tdmnodegraph.csv',encoding ="Latin-1") as sourceIn:
    sourceIn = csv.reader(sourceIn)
    headers = next(sourceIn)
    sources = [row for row in sourceIn]
G = nx.Graph() #creates a graph
import numpy as np
from itertools import combinations
pos = nx.random_layout(G)
sourceNode=[] #takes source and target edges
uniquesources = list(set([row[0]for row in sources]))
numberofunique=len(uniquesources)
#print(numberofunique)
i=0
##id=list(enumerate(uniquesources))
##keys = {source:i for i, source in enumerate(uniquesources)} 
#print (uniquesources)
with open('tdmunique.csv', 'w',encoding='Latin-1',newline='') as f:
      #head = getcsv(f, 4096, ';', '"');
      wtr = csv.writer(f)
      while i<numberofunique :
      #while i<5:
          #while i< 6:
          sourceNodeId=[]
          source=[]
          list=[]
          for row in sources:
              if(row[0] == uniquesources[i]):
                  sourceNodeId.append(row[1])
                  if(row[1] not in sourceNode):
                      count=0
                      wtr.writerow([row[1],count])
                      sourceNode.append(row[1])
                      source.append(row[1])
                      #print(source)
                  else:
                        list.append(row[1])
                        #print('exist'+row[1])
                        #print(list)
##                  elif(row[1] in sourceNode):
##                        count=row[1]
##                        print(count)
##                        #count=count+1
##                        print(row[1])
##                        wtr.writerow([row[1],count])
                  
              #wtr.writerow([sourceNodeId])
              G.add_nodes_from(sourceNode)
              merge = source+list
              edges = combinations(merge, 2)
              G.add_edges_from(edges)
          i=i+1
          #wtr.writerow([])
          #print(sourceNodeId)
          
          #print(list)
          #print(source)
          print(merge)
nx.draw_networkx(G)
plt.show(G)   
        
