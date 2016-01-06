import json
import nltk
#nltk.download()
from nltk.corpus import treebank
from itertools import islice
from nltk.grammar import PCFG, induce_pcfg, toy_pcfg1, toy_pcfg2
from nltk.tokenize import sent_tokenize, word_tokenize


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

def tweet_analysis():

    json_file = 'tweets.json'
    with open(json_file, 'r') as f:
        data = json.load(f)
        analysis(data)

tweet_analysis()
