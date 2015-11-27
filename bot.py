#by Shivang Patel
#Twitter_quote_bot

import json
import urllib2
import twitter
import time, sys

consumerKey = ''
consumerSecret = ''
accessTokenKey = ''
accessTokenSecret = ''

api = twitter.Api(consumer_key=consumerKey, consumer_secret=consumerSecret, access_token_key=accessTokenKey, access_token_secret=accessTokenSecret)

//checking container
CONTAINER = ''
WAITING_TIME=300 #5-min call
try:

    while True:
        #url = "http://api.theysaidso.com/qod.json?catagory"
        urlt ="http://quotesondesign.com/api/3.0/api-3.0.json"
        data = urllib2.urlopen(urlt)
        fd = json.load(data)
        //quote main container
        status = (fd["quote"])

        leng = len(status)

        if leng <= 140:
            #print "it is"
            #print status
            if status != CONTAINER:
                inst = api.PostUpdate(status)
            CONTAINER = status
        time.sleep(WAITING_TIME)
except:
    print "reloop"
    time.sleep(WAITING_TIME)
