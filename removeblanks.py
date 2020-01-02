import csv
import numpy
import networkx as nx
import matplotlib.pyplot as plt

with open('newstopword.csv',encoding ="Latin-1") as sourceIn:
    sourceIn = csv.reader(sourceIn)
    headers = next(sourceIn)
    sources = [row for row in sourceIn]
#uniquesources = list(set([row[0] for row in sources]))
#id=list(enumerate(uniquesources))
#keys = {source:i for i, source in enumerate(uniquesources)}   
links = []
with open('null.csv', 'w',encoding='Latin-1',newline='') as f:
      wtr = csv.writer(f)
      #operators = set(('a', 'b', 'use'))
      #stop = set(stopwords.words('english'))
      for row in sources:#
          #if re.match(r'^\s*$', row[3]):
          if row[2] == "" :
        
              wtr.writerow([row[0].lower(),row[1].lower(),row[2].lower()])

