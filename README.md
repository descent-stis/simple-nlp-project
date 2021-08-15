<h2 align="center">Simple NLP Project</h2>
<h3 align="center">A Sentiment Analysis Project for Beginner</h3>

## Requirements

There are some important libraries used in this project, such as:

```txt
googletrans
nltk
plotly
textblob
tweepy
wordcloud
```
More complete requirements at [here](requirements.txt).

## File Structure

```
.
├── data
├── functions
│   ├── preprocess.py
│   ├── save_data.py
│   ├── scrape_twitter.py
│   ├── sentiment.py
│   └── visualize.csv
├── hands_on.ipynb
├── requirements.txt
.
```

## File Description

There are some important files in this project, such as:

- `data` folder contains some saved data
- `functions` folder contains various functions and procedures
- `hands_on.ipynb` is the main program
- `requirements.txt`, list of libraries used in this project

## How to Use

To run the project locally, please do the following steps carefully.

1. Download this repo.
2. Install all libraries at the `requirements.txt`
3. Open `scrape_tweets.py` file. Then, fill in the blank tokens with your own tokens.

    ```python
    token = {'consumer_key'       : 'your consumer key',
             'consumer_secret'    : 'your consumer secret key',
             'access_token'       : 'your access token',
             'access_token_secret': 'your access secret token'}
    ```

4. Then move to `hands_on.ipynb` file, and run the notebook.

Meet Some Errors or Need a Help? Please contact [@myqrist](https://github.com/myarist)
