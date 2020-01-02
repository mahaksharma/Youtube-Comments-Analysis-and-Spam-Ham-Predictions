from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np

#word = pd.read_csv('tdmdata.csv',skiprows=1,header=None)
word = pd.read_csv('onevideo.csv',skiprows=1,header=None)
word.columns = ['video_id','user','comment']
print (word)

countvec = CountVectorizer()
countvec.fit_transform(word.comment)
a = pd.DataFrame(countvec.fit_transform(word.comment).toarray(), columns=countvec.get_feature_names())
a.to_csv('newpalak.csv')
print(a)
