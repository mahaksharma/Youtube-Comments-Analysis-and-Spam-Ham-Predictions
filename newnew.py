import csv
import numpy
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
commentno = pd.read_csv('tdmnode.csv',skiprows=1,header=None)
commentno.columns = ['term','comment']

df=pd.DataFrame(commentno)
i=0
from collections import Counter
grouped = df.groupby(['comment']).count()
print(grouped)
grouped.to_csv('complete1.csv')
