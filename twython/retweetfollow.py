#!/usr/bin/python

# Sample rudimentary script to search twitter for INFOSEC, retweet, and automatically follow user
# count is set to 1 for first search result, can be in multiple 

from twython import Twython, TwythonError 

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(consumer_key,consumer_secret,access_token, access_token_secret)

search_results = twitter.search(q='INFOSEC', count=1)
try:
    for tweet in search_results["statuses"]:
        try:
            twitter.retweet(id = tweet["id_str"])
            twitter.create_favorite(id = tweet["id_str"])
            st=tweet["entities"]["user_mentions"]
            if st != []:
                twitter.create_friendship(screen_name=st[0]["screen_name"])
        except TwythonError as e:
            print e
except TwythonError as e:
        print e
