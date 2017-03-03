import tweepy
import json
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler

with open('config.json') as file:
    config = json.load(file)

consumer_key = config['consumer_key']
consumer_secret = config['consumer_secret']
access_token = config['access_token']
access_secret = config['access_secret']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

#asd

class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                print("Write")
                return True
        except BaseException as e:
            print("Error")
        return True

    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=["#news"])