#!/usr/bin/python
#much of this code is borrowed from (looking for credit) 
#backdated to work with Python 2.7

import time
import datetime
import twython

from auth import (
	consumer_key,
	consumer_secret,
	access_token,
	access_token_secret
 )

MAXIMUM_TWEET_AGE = 120 # in days
SCREEN_NAME = "X"

twitter = twython.Twython(consumer_key,consumer_secret,access_token, access_token_secret)

def get_tweets():
	tweets = []
	ids = []

	start_time = time.time()
	end_time = start_time + 5
	# get tweets from your time line
	get_tweets = twitter.get_user_timeline(screen_name=SCREEN_NAME, count=200)
  	while True: # loop indefinitely
		for tweet in get_tweets: # add each tweet to the tweets list
			tweets.append(tweet)
		ids.append(tweet['id']) # add the last id
		get_tweets = twitter.get_user_timeline(screen_name=SCREEN_NAME, count=200, max_id=ids[-1])

		# if the last two IDs are the same, then there are no more tweets
		if len(ids) > 1 and ids[-1] == ids[-2]: # run into the end of tweets
			print "end of tweets break"
			break # break the loop

		elif time.time() >= end_time: # if you have been searching for more than 3 seconds
			print "end of time break"
			break # break the loop

	return tweets # return the tweets

for tweet in get_tweets():
	# get tweet's age in seconds
	age = time.time() - time.mktime(time.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y'))
	#print (tweet['created_at'])
	#print age
	days = age / 60 / 60 / 24

	if days > MAXIMUM_TWEET_AGE:
		try:
			twitter.destroy_status(id=tweet['id'])
			print "deleted: ", tweet['id'], days
		except:
			print "ERROR: %s" % id
			continue
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
print (st)
print ("end")
