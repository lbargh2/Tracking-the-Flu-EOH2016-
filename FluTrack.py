#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json, datetime, time
import tweepy

#Import from nltk
import json
import nltk
#nltk.download()
from nltk.corpus import treebank
from itertools import islice
from nltk.grammar import PCFG, induce_pcfg, toy_pcfg1, toy_pcfg2
from nltk.tokenize import sent_tokenize, word_tokenize


def print_tweets(api, filter, start_date, end_date, region, count):

    page = 1
    ct = 0
    deadend = False
    while True:
        # run api search
        tweets = tweepy.Cursor(api.search, q=filter, lang="en", locations=region,since=start_date, until=end_date).items(count)

        for tweet in tweets:
            #if (datetime.datetime.now() - tweet.created_at).days < 5: # example time stamp: 2015-11-24 02:13:33 or 2015-11-01
            #    #Do processing here:
            #    #print tweet.geocode
            print tweet.text.encode("utf-8")
            ct = ct + 1

            # exit clause
            if ct == count:
                return
            #else:
            #    deadend = True
            #    return
        if not deadend:
            page+=1
            time.sleep(500)

def write_tweets_to_json(api, filter, start_date, end_date, region, count, json_file):

    page = 1
    ct = 0

    list_of_tweets = []

    deadend = False
    while True:
        # run api search
        tweets = tweepy.Cursor(api.search, q=filter, lang="en", locations=region,since=start_date, until=end_date).items(count)

        for tweet in tweets:
            #if (datetime.datetime.now() - tweet.created_at).days < 5: # example time stamp: 2015-11-24 02:13:33 or 2015-11-01
            #    #Do processing here:
            #    #print tweet.geocode

            list_of_tweets.append(tweet.text.encode("utf-8"))

            #with open('tweets.json', 'a') as f:
            #     json.dump(tweet.text.encode("utf-8"), f)
            ct = ct + 1

            # exit clause
            if ct == count:
                print('three')
                with open(json_file, 'w') as f:
                     json.dump(list_of_tweets, f)
                return
            #else:
            #    deadend = True
            #    return
        if not deadend:
            page+=1
            time.sleep(500)


def tweetPull():

    # API stuff
    access_token = "97325888-4TiheE2EDlLRrRd0i3RyL99uIRMIjqOgMJilVWxsO"
    access_token_secret = "pHpBZnMavx1lTGA1UnS6Uzs6VvLJuwIBP7ExYXqbozoqg"
    consumer_key = "BuAsYJarW7WleTg0PrsvrrF2O"
    consumer_secret = "REOFH6Ue0vewobC1WILncfQrweqPIHc94JTjCBh3iuPhkckYPz"
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # filter words (array named "filter")
    file = open("filter.txt") # read in filter words from file named "filter.txt"; alter that file or just write it in here
    filter = file.readlines()
    file.close()
    for x in xrange(0, len(filter)):
        filter[x] = filter[x].strip()

    # dates to search within
    start_date = "2015-12-01" # year-mo-dy format
    end_date = "2016-01-05"

    # area of search
    region = [41.65,-79.67,44.91,-73.39] # set using coordinates (I think this is the state of New York atm)

    # desired number of tweets
    count = 20

    # json file to write to (if writing to file)
    json_file = 'tweets.json'

    ''' run function '''
    #print_tweets(api, filter, start_date, end_date, region, count)
    write_tweets_to_json(api, filter, start_date, end_date, region, count, json_file)

# Be aware that the program will not end after displaying the desired set of tweets at the moment.
# You will need to Ctrl-C or whatever manually for the time being

def analysis(tweet_list):
    symptoms = ['cough', 'fever','sick'] # need a better way to do this. shold probably write this into a json and read it when analyzing

    for tweet in tweet_list:

        tweet_score = 0

        words = word_tokenize(tweet)
        #tagged_words = nltk.pos_tag(words) # not sure what to use this for yet, but I think it's at least cool to have
        for word in words:
            tweet_score = tweet_score + symptomRecognition(word, symptoms)

        print(tweet)
        print(tweet_score)

def symptomRecognition(word, symptoms):
    symptoms1 = [symptoms[0], symptoms[1]]
    symptoms2 = [symptoms[2]]
    if word.lower() in symptoms1: # check lowercase word
        return 1
    if word.lower() in symptoms2:
        return 0.5
    return 0

def tweetAnalysis():

    json_file = 'tweets.json'
    with open(json_file, 'r') as f:
        data = json.load(f)
        analysis(data)

def main():

    tweetPull()
    tweetAnalysis()

main()
