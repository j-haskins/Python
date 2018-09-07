#!/usr/bin/python

# Sample rudimentary script to create a random tweet by combining a random word from (3) lists
# verbs.txt adjecttives.txt nouns.txt = random IT BS generator

import random

from twython import Twython
from auth import (
	consumer_key,
	consumer_secret,
	access_token,
	access_token_secret
 )

twitter = Twython(consumer_key,consumer_secret,access_token, access_token_secret)

verbs = open("verbs.txt").readlines()
adjectives = open("adjectives.txt").readlines()
nouns = open("nouns.txt").readlines()

first = random.choice(verbs).rstrip()
second = random.choice(adjectives).rstrip()
third = random.choice (nouns).rstrip()

message = first + " " + second + " " + third

twitter.update_status(status=message)
