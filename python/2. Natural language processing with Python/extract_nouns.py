# Author: @cephkhan (Ceph A. Khan)
# Extract nouns from text.

# import the TextBlob from textblob module
import nltk
from textblob import TextBlob

# Get text from user to extract nouns from
input_text = input("Enter text to extract nouns from: ")

blob = TextBlob(input_text)

# tags method returns an array of tuples. 
# Each tuple contains a word and 
# the word's corresponding part of speech
tags = blob.tags

# Using list comprehensions 
# with conditions to extract Proper Nouns,
# and nouns that have the NNP & NN tags respectively.
nouns = [
    word for (word, tag) in tags
    if ('NNP' == tag) or ('NN' == tag)
    ]

# Use enumerate to loop through lists with indices
for index, noun in enumerate(nouns):
    print(f"{index + 1 }. {noun}")
