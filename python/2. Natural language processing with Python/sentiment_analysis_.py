# Author: @cephkhan (Ceph A. Khan)
# PYTHON SCRIPT FOR SENTIMENT ANALYSIS

from textblob import TextBlob

def analyze_sentiment(text_to_analyze):
    # Creating a textblob object with the text to
    # analyze
    blob = TextBlob(text_to_analyze)
    
    # Running sentiment analysis on the text and
    # storing it's results in a sentiment_analysis var
    sentiment_analysis = blob.sentiment

    # Extracting the polarity attribute of the
    # analysis
    polarity = sentiment_analysis.polarity
    
    # Textblob returns a polarity attribute
    # Polarity is a value ranging between -1 to +1
    # Polarity=0 indicates a neutral sentiment
    # Polarity=-1 indicates very negative
    # Polarity=+1 indicates very positive

    # Classifying the sentiment as either Postitive, Negative or Neutral
    if polarity == 0:
        print(f'Text: {text_to_analyze}')
        print(f'Sentiment: Neutral\nPolarity: {polarity}\n')
    elif polarity > 0:
        if polarity <= 0.5:
            print(f'Text: {text_to_analyze}')
            print(f'Sentiment: Positive.\nPolarity: {polarity}\n')
        else: 
            print(f'Text: {text_to_analyze}')
            print(f'Sentiment: Very positive.\nPolarity: {polarity}\n')
    elif polarity < 0:
        if polarity >= -0.5:
            print(f'Text: {text_to_analyze}')
            print(f'Sentiment: Negative\nPolarity: {polarity}\n')
        else:
            print(f'Text: {text_to_analyze}')
            print(f'Sentiment: Very negative.\nPolarity: {polarity}\n')
    
analyze_sentiment("The food at Radison was very good.")
analyze_sentiment("Why are you sad?")
analyze_sentiment("Don't stop me now. I'm having such a good time.")
analyze_sentiment("You cant eat your cake and have it too.")
analyze_sentiment("This is the simplest NLP library.")
analyze_sentiment("Python is a good and easy programming language for beginners.")