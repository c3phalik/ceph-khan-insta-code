# Author: @cephkhan (Ceph A. Khan)
# PYTHON SCRIPT TO DETECT LANGUAGE

# import the TextBlob from textblob module & import pycountry
from textblob import TextBlob
import pycountry

# Get string input from user
string_to_detect = input('Type something in a random language:\n ')

# Create an instance of the TextBlob() object by passing in the user provided string
text_blob = TextBlob(string_to_detect)

# Using detect_language() method of the TextBlob() class to get the language's ISO code
lang_iso_code = text_blob.detect_language()

# We use pycountry package to get the full name of a language from it's ISO code
language = pycountry.languages.get(alpha_2=lang_iso_code)

# Finally we get the the full-name from the language object
detected_language = language.name

# Print the detected language
print(f'Language detected: {detected_language}')
