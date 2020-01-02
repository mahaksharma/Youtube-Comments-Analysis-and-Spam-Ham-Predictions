import csv
with open('idfuseful.csv',encoding ="Latin-1") as sourceIn:
    sourceIn = csv.reader(sourceIn)
    headers = next(sourceIn)
    sources = [row for row in sourceIn]
uniquesources = list([row[0] for row in sources])
#print(uniquesources)
#print(len(uniquesources))
with open('onevideo.csv',encoding ="Latin-1") as f:
    f = csv.reader(f)
    headers = next(f)
    sourcef = [row for row in f]
with open('usefulcomment.csv','w',encoding='Latin-1',newline='') as f1:
        wtr = csv.writer(f1)
        count=0
        for row in sourcef:
            #print(row[2])
            words=row[2].split()       
            #print(words)
            
            count=len(set(uniquesources)&set(words))
            
            if count>5:
                wtr.writerow([row[2],count])
            else:
                print(row[2],count)

       # print(row[2])
##if any(word in  for word in keyword_list):
##    print 'found one of em'
