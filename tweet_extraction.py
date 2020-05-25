import tweepy
import time
import pandas as pd

consumer_key = 'xxxxx'
consumer_secret = 'xxxxx'

""""Section 1: Get a preliminary collection of tweets in English"""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)
with open("out3.csv", "w", encoding='utf-8') as f:
   f.write("date,user_name,user_id,text,reply_to, retweet_count,favorite_count, retweet_status, user_mentions, hashtags\n")
for tweet in tweepy.Cursor(api.search, q='a', lang='en', until='2020-05-20').items():
    text = tweet.text
    remove_characters = [",", "\n", "\r", "\'"]
    for c in remove_characters:
        text = text.replace(c, " ")
    print(repr(text))
    reply_to = "None"
    if hasattr(tweet, "in_reply_to_screen_name"):
        reply_to = tweet.in_reply_to_screen_name
    retweet = False
    if hasattr(tweet, "retweeted_status"):
        retweet = True
    user_mentions = "None"
    if hasattr(tweet.entities, "user_mentions"):
        user_mentions = tweet.entities.user_mentions
    hashtags = "None"
    if hasattr(tweet.entities, "hashtags"):
        hashtags = tweet.entities.hashtags
    if not tweet.truncated:
        with open("out3.csv", "a", encoding='utf-8') as f:
            f.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (
            tweet.created_at, tweet.user.screen_name, tweet.user.id, text, reply_to, tweet.retweet_count,
            tweet.favorite_count, retweet, user_mentions, hashtags))

""""Section 2: Extract multiple tweets per user id"""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)
df = pd.read_csv("out3.csv")
user_names = df.user_name.unique()
with open("out_per_id2.csv", "w", encoding='utf-8') as f:
    f.write("date,user_name,user_id,text,reply_to, retweet_count,favorite_count, retweet_status, user_mentions, hashtags\n")
for name in user_names:
   try:
        for tweet in tweepy.Cursor(api.user_timeline, screen_name=name).items(1000):
            text = tweet.text
            remove_characters = [",", "\n", "\r", "\'"]
            for c in remove_characters:
                text = text.replace(c, " ")
            print(repr(text))
            reply_to = "None"
            if hasattr(tweet, "in_reply_to_screen_name"):
                reply_to = tweet.in_reply_to_screen_name
            retweet = False
            if hasattr(tweet, "retweeted_status"):
                retweet = True
            user_mentions = "None"
            if hasattr(tweet.entities, "user_mentions"):
                user_mentions = tweet.entities.user_mentions
            hashtags = "None"
            if hasattr(tweet.entities, "hashtags"):
                hashtags = tweet.entities.hashtags
            if tweet.lang=='en' and not tweet.truncated:
                print("success!")
                print(tweet.text)
                with open("out_per_id2.csv", "a", encoding='utf-8') as f:
                    f.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (
                        tweet.created_at, tweet.user.screen_name, tweet.user.id, text, reply_to, tweet.retweet_count,
                        tweet.favorite_count, retweet, user_mentions, hashtags))
        time.sleep(20)
   except tweepy.error.TweepError as exception:
       print("Could not retrieve tweets for user " + str(name))




