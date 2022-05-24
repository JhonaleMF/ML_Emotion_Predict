import snscrape.modules.twitter as sntwitter
import pandas as pd
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
query = "@TheBridge_Tech until:2022-05-24 since:2022-01-01"
tweets = []
limit = 4000


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.id, tweet.content, tweet.date, tweet.user.id, tweet.user.displayname, tweet.user.username, tweet.retweetCount, tweet.replyCount, tweet.likeCount, tweet.quoteCount])
        
df = pd.DataFrame(tweets, columns=['Id_tweet', 'Texto', "Fecha", 'Id_autor', "Nombre_autor", "username_autor", "N_Retweet", "N_Reply", "N_Like", "N_Quote"])
df.to_csv("twitter.csv")
print(df)