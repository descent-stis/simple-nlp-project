def save_data(tweet_data, topik):
    
    tweet_data.to_csv(f"data/{topik}.csv", index = False, header = True)
    tweet_data.to_excel(f"data/{topik}.xlsx", index = False, header = True)
    
    print('✅ Success')