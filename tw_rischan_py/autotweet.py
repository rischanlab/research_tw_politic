__author__ = 'rischan'

import constants
from db_conn import DBConn
from random import randint
from datetime import datetime
import time
from util import setup_api

# constants
consumer_key = constants.consumer_key
consumer_secret = constants.consumer_secret
access_key = constants.access_key
access_secret = constants.access_secret



def main():
    local_tz = time.timezone / (60 * 60)
    #autotweet at the working time (indonesia)
    current_hour = (datetime.now().hour + (7 + local_tz)) % 24  # to GMT +7
    if 0 < current_hour < 5:
        print 'too late to tweet'
        return
    api = setup_api(consumer_key, consumer_secret, access_key, access_secret)

    dbconn = DBConn()
    post_table = 'tw' #name of table 
    name_column = 'tweet' #name of column
    q_num_post = 'SELECT COUNT(*) FROM ' + post_table #count the rows of data
    num_post = dbconn.read(q_num_post)
    numb_post =num_post[0][0] #get value from count of rows data
    #print num_post[0][0]

    #query for select tweets
    query = 'SELECT ' + name_column + ' FROM ' + post_table
    a = dbconn.read(query)
    rand_number = randint(0, numb_post)

    api.update_status(str(a[rand_number][0]))

if __name__ == '__main__':
    main()
