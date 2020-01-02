import csv
with open('complete1.csv',encoding ="Latin-1") as sourceIn:
    sourceIn = csv.reader(sourceIn)
    headers = next(sourceIn)
    sources = [row for row in sourceIn]
import numpy as np
import math
##with open('completespam.csv', 'w',encoding='Latin-1',newline='') as f1:
##    wtr1 = csv.writer(f1)

with open('completespamgraph.csv', 'w',encoding='Latin-1',newline='') as f:
    wtr = csv.writer(f)
    i=0
    sum=0
    for row in sources:
        denom = int(row[1])**2
        sum= sum+denom
    for row in sources:
        sqr=(int(row[1]) / math.sqrt(sum))
        #wtr.writerow([row[0],row[1],sqr])
        if sqr <= 0.01946181:
            #wtr1.writerow([row[0],row[1],sqr])
            wtr.writerow([row[0],row[1],sqr])
            
        else:
            
            print (sqr)
            #print (sqr)
        
