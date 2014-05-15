
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


#this program is for random tweet and delete the data in the table after updated

def main():
    local_tz = time.timezone / (60 * 60)
    current_hour = (datetime.now().hour + (7 + local_tz)) % 24  # to GMT +7
    if 0 < current_hour < 5:
        print 'too late to tweet'
        return
    api = setup_api(consumer_key, consumer_secret, access_key, access_secret)

    dbconn = DBConn()
    post_table = 'tw'
    id_column = 'id'
    name_column = 'tweet'
    q_num_post = 'SELECT COUNT(*) FROM ' + post_table #calculate the total of rows data in the table
    num_post = dbconn.read(q_num_post)
    numb_post = num_post[0][0]
    #print num_post[0][0]

    query = 'SELECT ' + id_column + ',' + name_column + ' FROM ' + post_table #query for selecting the data tweet in the table
    a = dbconn.read(query)
    rand_number = randint(0, numb_post) #generate random number for randoming the data
    id_status = str(a[rand_number][0])
    status = str(a[rand_number][1])
    print id_status, status
    api.update_status(status) #for update status (tweet)
    query_delete = 'DELETE FROM ' + post_table + ' WHERE ' + id_column + ' = ' + id_status #query for deleting the data tweet in the table after updated
    ex = dbconn.delete(query_delete)
    print ex

if __name__ == '__main__':
    main()