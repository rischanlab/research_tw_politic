__author__ = 'rischan'

import constants
from datetime import datetime
import time
from util import setup_api
import tweepy
from tweepy import Cursor, TweepError
import sys

# constants
consumer_key = constants.consumer_key
consumer_secret = constants.consumer_secret
access_key = constants.access_key
access_secret = constants.access_secret

def main():
    api = setup_api(consumer_key, consumer_secret, access_key, access_secret)
    print "Loading followers.."
    followers = []
    for follower in tweepy.Cursor(api.followers).items():
        followers.append(follower)

    print "Found %s followers, finding friends.." % len(followers)
    friends = []
    for friend in tweepy.Cursor(api.friends).items():
        friends.append(friend)

    friend_dict = {}
    for friend in friends:
        friend_dict[friend.id] = friend

    follower_dict = {}
    for follower in followers:
        follower_dict[follower.id] = follower

    non_friends = [friend for friend in friends if friend.id not in follower_dict]

    print "Unfollowing %s people who don't follow you " % len(non_friends)
    print "This will take approximately %s minutes." % (len(non_friends) / 60.0)
    answer = raw_input("Are you sure? [Y/n]").lower()
    if answer and answer[0] != "y":
        sys.exit(1)

    for nf in non_friends:
        print "Unfollowing %s" % nf.screen_name
        try:
            nf.unfollow()
        except:
            print "  .. failed, sleeping for 5 seconds and then trying again."
            time.sleep(5)
            nf.unfollow()
        print " .. completed, sleeping for 1 second."
        time.sleep(1)

if __name__ == '__main__':
    main()