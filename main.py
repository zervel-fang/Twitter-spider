######## author: fang zhou
######## email: zervel3@std.uestc.edu.cn
import pandas as pd
import tweepy
import csv
import requests
from urllib.request import getproxies
import emoji
import re
x=getproxies()
print(x)
#### set your key  and secrets, where you can access by applying a twitter developer account
consumer_key = 'xxxx'
consumer_secret = 'xxxx'
access_token = 'xxxx'
access_secret = 'xxxx'
def retrieve_tweets(input_file,outputfile):
    # Authorization with Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=10, retry_delay=5,
                     retry_errors=set([401, 404, 500, 503]),proxy=x['https'])
    fid1 = open(input_file, 'r')
    i  = 0
    sumv = 0
    tweet_id_list = []
    fid = open(outputfile,'a+',encoding='utf-8')
    myre = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U0001F1F2-\U0001F1F4"  # Macau flag
        u"\U0001F1E6-\U0001F1FF"  # flags
        u"\U0001F600-\U0001F64F"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U0001F1F2"
        u"\U0001F1F4"
        u"\U0001F620"
        u"\u200d"
        u"\u2640-\u2642"
        "]+", flags=re.UNICODE)
    for j in fid1:
        #print(j)
        j = j.strip('\n')
        #print(j)
        tweet_id_list.append(j)
        i = i + 1
        if i==100:
            #print(tweet_id_list)
            sumv = sumv + i
            print(sumv)
            tag=1
            while tag==1:
                try:
                    tweets = api.statuses_lookup(tweet_id_list)
                    tw_list =list(tweets)
                    for ii in tw_list:
                        text = myre.sub(r'', ii.text)
                        text = text.replace("\n", " ")
                        text1 = myre.sub(r'', ii.user.name)
                        fid.write(text1 + '>>::<<' + str(ii.user.id) + '>>::<< ' + str(ii.created_at) + '>>::<< ' + text + '\n')
                        fid.flush()
                    i = 0
                    tag = 0
                except Exception as e:
                    print(e)
            del tweet_id_list
            tweet_id_list = []

    ## deal with the remaining parts
    tag = 1
    while tag == 1:
        try:
            tweets = api.statuses_lookup(tweet_id_list)
            tw_list = list(tweets)
            for ii in tw_list:
                text = myre.sub(r'', ii.text)
                text = text.replace("\n", " ")
                text1 = myre.sub(r'', ii.user.name)
                fid.write(text1 + '>>::<<' + str(ii.user.id) + '>>::<< ' + str(ii.created_at) + '>>::<< ' + text + '\n')
                fid.flush()
            i = 0
            tag = 0
        except Exception as e:
            print(e)

retrieve_tweets('tweet_id/2020-03-31-dataset.txt','results/2020-03-23-dataset.txt')
retrieve_tweets('tweet_id/2020-04-01-dataset.txt','results/2020-03-24-dataset.txt')
retrieve_tweets('tweet_id/2020-03-25-dataset.txt','results/2020-03-25-dataset.txt')
retrieve_tweets('tweet_id/2020-03-26-dataset.txt','results/2020-03-26-dataset.txt')
retrieve_tweets('tweet_id/2020-03-27-dataset.txt','results/2020-03-27-dataset.txt')
retrieve_tweets('tweet_id/2020-03-28-dataset.txt','results/2020-03-28-dataset.txt')
retrieve_tweets('tweet_id/2020-03-29-dataset.txt','results/2020-03-29-dataset.txt')
