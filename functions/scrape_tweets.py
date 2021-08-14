import pandas as pd
import tweepy as tw

def get_token():
    
    token = {'consumer_key'         : 'your consumer key',
             'consumer_secret'      : 'your consumer secret key',
             'access_token'         : 'your access token',
             'access_token_secret'  : 'your access secret token'}
    
    return token

def get_api(token):
    
    auth = tw.OAuthHandler(token['consumer_key'], token['consumer_secret'])
    auth.set_access_token(token['access_token'], token['access_token_secret'])
    api = tw.API(auth, wait_on_rate_limit = True)
    
    print('✅ Connected')
    
    return api

def get_tweets(api, search_word, num):
    
    print(f'⏳ Looking for the topic "{search_word}" as much as {num} ...')
    
    new_search = search_word + " -filter:retweets"

    tweets = tw.Cursor(
        api.search, 
        q                = new_search,
        result_type      = "mixed",
        lang             = "en",
        count            = 20,
        include_entities = True,
        since_id         = "2021-06-01"
    ).items(num)

    data = [
        [tweet.created_at,
         tweet.author.screen_name,
         tweet.author.name,
         tweet.text,
         tweet.retweet_count,
         tweet.favorite_count,
         tweet.user.location
    ] for tweet in tweets]

    tweet_data = pd.DataFrame(
        data = data, 
        columns = ["date", 
                   "user", 
                   "name", 
                   "text", 
                   "retweet", 
                   "favorite", 
                   "location"]
    )
    
    print(f'✅ Success, we find {tweet_data.shape[0]} data about "{search_word}"')
    
    return tweet_data