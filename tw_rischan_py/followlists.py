__author__ = 'rischan'

import tweepy
import constants
from datetime import datetime
from util import is_up2date, is_good_account, setup_api, read_list

# constants
consumer_key = constants.consumer_key
consumer_secret = constants.consumer_secret
access_key = constants.access_key
access_secret = constants.access_secret


def test():
    a = datetime.now()
    print is_up2date(a)


def main():
    api = setup_api(consumer_key, consumer_secret, access_key, access_secret)
    file_path = 'Name of List accounts'
    accounts = read_list(file_path)
    for account in accounts:
	try:
		friend = api.create_friendship(account)
		if friend.screen_name == account:
			print 'Follow ' + account + ' success'
		else:
			print 'Follow ' + account + ' failed'
	except tweepy.TweepError, e:
		print e

if __name__ == '__main__':
	main()
