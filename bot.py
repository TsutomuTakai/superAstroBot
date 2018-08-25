import tweepy
import csv
import tkinter
import urllib
import _thread
import random
from credentials import *
from time import sleep

def updUsers():
    dat = open('collabUsers.txt','r')
    collabUsers = dat.readlines()
    dat.close()
    collabUsers = [x.strip() for x in collabUsers]
    collabUsers = [int(x) for x in collabUsers]
    return collabUsers

def tenMinuteThread():
    while 1:
        collabUsers = updUsers()
        search = "#astrominibr"
        numberOfTweets = 500
        #print(collabUsers)
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            #print(tweet.user.id in collabUsers, tweet.user.id)
            if(tweet.user.id in collabUsers):
                
                try:				
                    tweet.retweet()
                    #print('retweet')
                except tweepy.TweepError as e:
                    print(e.reason)
					
                except StopIteration:
                    break

        for tweet in tweepy.Cursor(api.search, "apod").items(50):
            if(tweet.user.id == "8295072"):
                try:
                    tweet.retweet()
                except tweepy.TweepError as e:
                    print(e.reason)
                except StopIteration:
                    break

        sleep(1800)
    

def thirtyMinuteThread():
    tweetDB =getTDB()
    while 1:
        
        #print(tweetDB)
        if( len(tweetDB) == 0):
            tweetDB =getTDB()
        index = random.randint(0, len(tweetDB)-1)
        if( tweetDB[index][1] == ''):
            api.update_status(tweetDB[index][0])
        else:
            file = 'img/' + tweetDB[index][1]
            api.update_with_media(file, status=tweetDB[index][0])
        tweetDB.pop(index)
        sleep(3600)

def getTDB():
    csv.register_dialect('myDialect',
    delimiter = ';',
    quoting=csv.QUOTE_ALL,
    skipinitialspace=True)
    with open('teste.txt', mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, dialect='myDialect')
        tweetDB = list(csv_reader)
        return tweetDB    
            
    

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)

try:
    _thread.start_new_thread( tenMinuteThread, () )
    _thread.start_new_thread( thirtyMinuteThread , ())
except:
    print('Erro ao gerar processo')
##
##while 1:
##    pass


