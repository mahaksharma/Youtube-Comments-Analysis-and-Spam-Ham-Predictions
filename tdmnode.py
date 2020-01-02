import csv
import numpy
import networkx as nx
import matplotlib.pyplot as plt

with open('newpalak.csv',encoding ="Latin-1") as sourceIn:
    sourceIn = csv.reader(sourceIn)
    headers = next(sourceIn)
    sources = [row for row in sourceIn]

#uniquesources = list(set([row[0] for row in sources]))
#id=list(enumerate(uniquesources))
#keys = {source:i for i, source in enumerate(uniquesources)}   
links = []
label=len(headers)
print (label)
#if sour == 'True':
    #print (row[3],row[2])
    
    #source = (row for row in sourceIn if row not in row[3] )
with open('tdmnode.csv', 'w',encoding='Latin-1',newline='') as f:
      #head = getcsv(f, 4096, ';', '"');
      wtr = csv.writer(f)
      i =1
      count =0
      #word = pd.read_csv('onevideo.csv',skiprows=1,header=None)
      while i < label:
          for row in sources:
              if row[i] != '0':
                  count +=1
                  wtr.writerow([headers[i],row[0]])
          i=i+1
              #print(headers[1])    
              #print(count)     
  
##G = nx.Graph() #creates a graph
##pos = nx.random_layout(G)
##sourceNodeId=[] #takes source and target edges
##for row in id:
## sourceNodeId.append(row[0])
##G.add_nodes_from(sourceNodeId)#creates nodes for the graph.
###print("Total number of video nodes are:", G.number_of_links())
##for node in links:
## edges = list(node.items())
## G.add_edge(*edges[0])
##nx.draw_networkx(G)
##plt.show(G)   
        
