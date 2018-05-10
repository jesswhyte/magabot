#!/usr/bin/env python
#Magabot will look for tweets with the Make America Great Again hashtag (#maga) + [bitch,cunt,slut,whore]
#Magabot will then read them aloud to you. 
#Run it in the background while you work for a great day!

#And remember, the stream API represents just a small fraction
#of the actual tweets that go out every minute. 

import json
import os
import re

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API
# Go to dev.twitter.com, using your twitter account, you will need to set up
# an "app" in order to get your API keys and tokens
CONSUMER_KEY = 'yourkeygoeshere' #or, better yet, somewhere else
CONSUMER_SECRET = 'yoursecretconsumerkeygoeshere' #or, better yet, somewhere else
ACCESS_TOKEN = 'youraccesstokengoeshere' #or, better yet, somewhere else
ACCESS_SECRET = 'yoursecretaccesstokengoeshere' #or, better yet, somewhere else

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

#you can change the search terms here, but why would you? FUN!!!
iterator = twitter_stream.statuses.filter(track="#maga slut,#maga bitch,#maga whore, #maga cunt", language="en")
           
# Here we set it to stop after getting 100 tweets. 
# You don't have to set it to stop 
tweet_count = 100


for tweet in iterator:
    tweet_count -= 1
# Print each tweet in the stream to the screen 
    # to convert it back to the JSON format to print/score
    #print json.dumps(tweet)  
    
       
    if 'text' in tweet: # only messages contains 'text' field is a tweet
            #print 'http://twitter.com/statuses/%i' %tweet['id']
            print tweet['id'] # This is the tweet's id
            print tweet['created_at'] # when the tweet posted
            print tweet['user']['name'] # name of the user
            print tweet['user']['screen_name'] # name of the user account
            print tweet['text'] # content of the tweet
            #convert tweet text to unicode so flite can read it
            tweettext=unicode(tweet['text']).encode('utf-8')
            #take out the URLs using regex because they're weird
            tweettext=re.sub(r"http\S+","", tweettext)

    #read the tweets using flite...p.s. you have to install flite
    #sudo apt-get install flite
    os.system("flite -voice slt -t 'Incoming:"+tweettext+"ALL DONE'")
    #time.sleep(5)
                      
    if tweet_count <= 0:
        break


