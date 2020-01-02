import csv
import numpy
import networkx as nx

with open("testlatin.csv", "r",encoding ="Latin-1") as infile, open("finalpunc.csv",'w',encoding='Latin-1',newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    conversion = set(',.?!"-():;')
    for row in reader:
        newrow = [''.join(' ' if c in conversion else c for c in entry) for entry in row]
        writer.writerow(newrow)
