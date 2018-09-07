#!/usr/bin/python

# Rudimentary script for following all followers and unfollowing non-followers
# For accounts with < 5000 followers

import sys

from twython import Twython
from auth import (
	consumer_key,
	consumer_secret,
	access_token,
	access_token_secret
 )

twitter = Twython(consumer_key,consumer_secret,access_token, access_token_secret)
twitter_name = "CHANGE TO TWITTER NAME"

# Retrieve all followers for a given screen name, store in text file followers.txt
def get_followers():
	f1 = open('followers.txt', 'w')
	followers = twitter.get_followers_ids(screen_name = twitter_name ) 
	for follower_id in followers['ids']:
		f1.write(' '.join(( str(follower_id), '\n' )))
	f1.close()

# Retrieve all friends (following) for a given screen name, store in text file friends.txt
def get_friends():
	f2 = open('friends.txt', 'w')
	friends = twitter.get_friends_ids(screen_name = twitter_name)
	for friend_id in friends['ids']:
		f2.write(' '.join(( str(friend_id), '\n' )))
	f2.close()

# Derive which friends NOT following (and follow) via load followers and friends into lists
def follow_friends():
	with open('followers.txt') as f3:
		fing = f3.read().splitlines()
	with open('friends.txt') as f4:
		fwers = f4.read().splitlines()
	get_names = [x for x in fing if x not in fwers]
	for item in get_names:
		try:
			print "create friendship with ID: %s" % item	
			twitter.create_friendship(id = item)
		except:
			print "ERROR: %s" % item
			continue

# Derive who does not follow back and destroy friendship via lists
def unfollow():
	with open('followers.txt') as f3:
		fing = f3.read().splitlines()
	with open('friends.txt') as f4:
		fwers = f4.read().splitlines()
	get_names = [x for x in fwers if x not in fing]	
	for item in get_names:
		twitter.destroy_friendship(id = item)
		print "destroy friendship with ID: %s" % item	

def main():
	get_followers()
	get_friends()
	follow_friends()
	unfollow()
 
main()
print "END"
