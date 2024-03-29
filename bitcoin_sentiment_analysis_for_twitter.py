# -*- coding: utf-8 -*-
"""Bitcoin Sentiment Analysis for Twitter.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11ceDwqNueF8Txg-KGPS4fsAj-x0iGZrY
"""

import tweepy
from textblob import TextBlob
import pandas as pd
import numpy as np
import re #regular expressions
import matplotlib.pyplot as plt

from google.colab import files
files.upload()

df= pd.read_csv('Tweets.csv')
df.head()

df.corr()

def cleanTwt(text):
    if isinstance(text, str):
        text= re.sub('#bitcoin','bitcoin',text) #Removes the "#" from bitcoin
        text= re.sub('#Bitcoin','Bitcoin',text) #Removes the "#" from Bitcoin
        text= re.sub('#[A-Za-z0-9]+','',text) #Removes the "#" from any string
        text= re.sub('\\n','',text) #Removes the "\n" string
        text= re.sub('https?:\/\/\S+','',text) #Removes the hyperlinks

        return text.lstrip('#')
    else:
        return str(text)

#Clean the tweets
df['Cleaned_Tweets'] = df['Text'].astype(str).apply(cleanTwt)
df.head()

def getSubjectivity(text):
  return TextBlob(text).sentiment.subjectivity

def getPolarity(text):
  return TextBlob(text).sentiment.polarity

df['Subjectivity']=df['Cleaned_Tweets'].apply(getSubjectivity)
df['Polarity']=df['Cleaned_Tweets'].apply(getPolarity)

df.head()

def getSentiment(score):
  if score <0:
    return 'Negative'
  elif score==0:
    return 'Neutral'
  else :
    return 'Positive'

df['Sentiment']=df['Polarity'].apply(getSentiment)
df.head()

df['Sentiment'].value_counts().plot(kind='bar')
plt.title('Sentiment Analysis Plot')
plt.xlabel('Sentiment')
plt.ylabel('Numbor of Tweets')
plt.show()

