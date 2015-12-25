import nltk
#nltk.download()
from nltk.corpus import treebank
from itertools import islice
from nltk.grammar import PCFG, induce_pcfg, toy_pcfg1, toy_pcfg2
from nltk.tokenize import sent_tokenize, word_tokenize

import json

#nltk.parse.chart.demo(2, print_times=False, trace=0,sent='I saw a dog', numparses=1)
#tokens = "Jack saw Bob with my cookie".split()
#grammar = toy_pcfg2
#print(grammar)


EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."

words = word_tokenize(EXAMPLE_TEXT)
tagged_words = nltk.pos_tag(words)

# writing json file
with open('data.json', 'w') as f:
     json.dump(tagged_words, f)

print(tagged_words[1][1])

# reading json file
with open('data.json', 'r') as f:
     data = json.load(f)
     print data[1][1]
