from wordcloud import WordCloud

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import plotly as py

def get_distribution(tweet_data):
    
    tweet_time = pd.to_datetime(tweet_data['date'], format='%Y-%m-%d')

    trace = go.Histogram(
        x       = tweet_time,
        marker  = dict(color = 'blue'),
        opacity = 0.75
    )

    layout = go.Layout(
        title   = 'Tweet Distribution',
        height  = 450,
        width   = 1200,
        xaxis   = dict (title = 'Date and Month'),
        yaxis   = dict(title = 'Tweet Quantity'),
        bargap  = 0.2,
    )
    
    fig = go.Figure(data = [trace], layout = layout)
    py.offline.iplot(fig)
    
def get_wordcloud(tweet_data, column):
    
    text = tweet_data[column]
        
    wordcloud = WordCloud(background_color='black',
                          contour_width = 5, 
                          contour_color = 'black'
    ).generate(str(text))

    plt.figure(figsize=(30, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()