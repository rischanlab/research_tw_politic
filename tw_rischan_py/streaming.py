
from slistener import SListener
import time, tweepy, sys

## auth. 
## TK: Edit the username and password fields to authenticate from Twitter.
#username = ''
#password = ''
#auth     = tweepy.auth.BasicAuthHandler(username, password)
#api      = tweepy.API(auth)

## Eventually you'll need to use OAuth. Here's the code for it here.
## You can learn more about OAuth here: https://dev.twitter.com/docs/auth/oauth
#this consumer key from rischan mafrur twitter account the name is research twitter

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def main():
    track = ['#TolakPartaiPoligami']
 
    listen = SListener(api, 'TolakPartaiPoligami')
    stream = tweepy.Stream(auth, listen)

    print "Streaming started..."

    try: 
        stream.filter(track = track)
    except:
        print "error!"
        stream.disconnect()

if __name__ == '__main__':
    main()