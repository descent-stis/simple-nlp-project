from googletrans import Translator

from textblob import TextBlob

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

def get_similarity(tweet_prep, column):
    senti = tweet_prep.loc[:10, [column]]
    senti['polarity'] = pd.DataFrame(senti[column]).apply(lambda x: TextBlob(x[column]).sentiment.polarity, axis = 1)
    senti

def analize_sentiment(tweet):
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1
    
def showPieChart(positive, neutral, negative):
    pc = plt.figure(figsize = (7, 7))
    plt.pie([positive, neutral, negative],
            autopct = '%1.1f%%', 
            colors = ['green','white','red'], 
            explode = (0.1, 0.1, 0.1), 
            startangle = 140)
    plt.show()

def get_sentiment(tweet_prep, column):
    
    get_similarity(tweet_prep, column)
    
    senti = tweet_prep.loc[:, [column]]
    senti['sentiment'] = np.array([analize_sentiment(tweet) for tweet in senti[column]])

    pos_tweets = [tweet for index, tweet in enumerate(senti[column]) if senti['sentiment'][index] > 0]
    neu_tweets = [tweet for index, tweet in enumerate(senti[column]) if senti['sentiment'][index] == 0]
    neg_tweets = [tweet for index, tweet in enumerate(senti[column]) if senti['sentiment'][index] < 0]

    showPieChart(positive=len(pos_tweets), neutral=len(neu_tweets), negative=len(neg_tweets))
    
    return pos_tweets, neu_tweets, neg_tweets

def get_tweets_sentimen(pos, neu, neg):
    
    translator = Translator()
    
    print(f'\n🟢 Positive \n{translator.translate(pos[random.randint(0, len(pos))], dest="id").text} \n')
    
    print(f'⚪ Neutral \n{translator.translate(neu[random.randint(0, len(neu))], dest="id").text} \n')
    
    print(f'🔴 Negative \n{translator.translate(neg[random.randint(0, len(neg))], dest="id").text}')