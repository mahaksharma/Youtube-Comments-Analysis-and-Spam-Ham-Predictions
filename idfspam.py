import csv
with open('tfidfanalysis.csv',encoding ="Latin-1") as sourceIn:
    sourceIn = csv.reader(sourceIn)
    headers = next(sourceIn)
    sources = [row for row in sourceIn]
import numpy as np
import math
with open('idfspam.csv', 'w',encoding='Latin-1',newline='') as f:
        wtr = csv.writer(f)
        i=0
        sum=0
        for row in sources:
            denom = float(row[1])**2
            sum= sum+denom
        for row in sources:
            sqr=(float(row[1]) / math.sqrt(sum))
            if sqr > 0.02262999:
                wtr.writerow([row[0],row[1],sqr])
            else:
                print(sqr)
                
