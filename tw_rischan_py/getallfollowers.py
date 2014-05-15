__author__ = 'rischan'


import tweepy
import constants
import time
from datetime import datetime
from tweepy import Cursor, TweepError
from util import is_up2date, is_good_account, setup_api

# constants
consumer_key = constants.consumer_key
consumer_secret = constants.consumer_secret
access_key = constants.access_key
access_secret = constants.access_secret


def test():
    a = datetime.now()
    print is_up2date(a)


def main():
    ids = []
    listfollowers =[]
    i =0
    save_file = open("list_followers.txt","rw+")
    api = setup_api(consumer_key, consumer_secret, access_key, access_secret)
    for page in tweepy.Cursor(api.followers,screen_name="NameofAccount").pages():
        i +=1
	#use cursor for bypass 20 view limit from twitter
        while len(page) >0:
            listfollowers = page.pop()
            if is_good_account(listfollowers):
                print>> save_file,listfollowers.screen_name
                print listfollowers.screen_name
        ids.extend(page)
        time.sleep(60)
    #print len(ids)


if __name__ == '__main__':
    main()
  
