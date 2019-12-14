# Author: @cephkhan (Ceph A. Khan)
# PYTHON SCRIPT TO TRANSLATE TO ANY LANGUAGE

# import the TextBlob from textblob module
from textblob import TextBlob

# Fetch a string from the user
string_to_translate = input('\nEnter something to be translated: ')

# Create an instance of TextBlob
text_blob = TextBlob(string_to_translate)

# To translate text we call .translate() 
# method on the TextBlob object 
# and pass in a keyword argument 'to=LANG' 

# To translate to Hindi call .translate(to='hi')
hindi = text_blob.translate(to='hi')
print(f'\nHindi translation: {hindi}') 

# Set to='fr' for french translation
french = text_blob.translate(to='fr')
print(f'\nFrench translation: {french}\n')

# Set to='zh-CN' for simplified chinese
chinese = text_blob.translate(to='zh-CN')
print(f'\nChinese translation: {chinese}\n')
