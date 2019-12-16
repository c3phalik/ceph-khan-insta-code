"""
Author: Ceph A. Khan

Series: Using BeautifulSoup to scrap data from HTML

Description: 
Python program to demonstrate
extracting data from HTML Markup.

We will scrape Top 10 Google results in this program.

"""
# Run pip install beautifulsoup4
# to get the beautiful soup module.
# import BeautifulSoup & request modules
from bs4 import BeautifulSoup
import requests as r

# Enter the search to scrape Google for
search_term = input('Enter your search term:')

# Building the Google search URL
# It's really simple. Adding a 'q' url parameter
# does the trick.
search_url = f'https://google.com/search?q={search_term}'

# Set headers to mimic a real browser
# if you fail to do this, websites won't
# serve their web-pages to you
headers = {'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/61.0.3163.100 Safari/537.36'
            }

# Now you've got to use the requests module
# Sending a get request to the previously
# defined search url will return the Google search results
response = r.get(search_url, headers=headers)

# Getting the markup from Google's search results
search_result_markup = response.text

# Diving in to BeautifulSoup
soup = BeautifulSoup(search_result_markup, 'lxml')

# Google displays all the search results in a .rc div element
# We are using BeautifulSoup's .find_all() method to get a list
# of all the divs with class 'rcc'. Thus, scraping its result.
results = soup.find_all('div', class_='rc')

# The div.rcc has two more divs with seperate classes
# |-div.r => Stores the headline & URL of the search result
# |
# |-div.s => Stores the description of the search result

# We will traverse the main search result element to find the 
# child elements div.r and div.s. Remeber, div.rcc is stored
# in the results variable. So, let's run a for loop.
for result in results:
    # Using BeautifulSoup's .find() method to extract the 
    # child which contains headline & URL
    headline_div = result.find('div', class_='r')
    # Extracting the child div element which contains
    # the description of search result.
    description_div = result.find('div', class_='s')
    
    # Google uses the h3 tag for it's search result headlines.
    # .find method can locate the 'h3' element and .text attribute 
    # returns the text of the h3 element. 
    # Headline => SCRAPED 😎
    headline = headline_div.find('h3').text

    # .find method to locate the anchor tag element and
    # using the .get method from BeautifulSoup to fetch it's URL
    # URL => Scraped 😎
    url = headline_div.find('a').get('href')

    # Inside the description_div, Google stores another div element
    # Which stores another 'span' element. We use the .find method
    # successively on the children to find the respective div & span
    # .text returns the text of the description
    # Description => Scraped 😎
    description = description_div.find('div').find('span').text

    # Now lets print each result and see the output in the following pages
    print(f'\nHeadline: {headline}\nUrl: {url}\ndesciption: {description}\n')