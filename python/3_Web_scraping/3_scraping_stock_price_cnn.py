"""
Author: Ceph A. Khan
Series: Web-scraping with Python
A very basic program to scrape latest 
stock pricess from CNN.com
"""

import requests
from bs4 import BeautifulSoup

# Set headers to mimic a real browser
# if you fail to do this, websites won't
# serve their web-pages to you
headers = {'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/61.0.3163.100 Safari/537.36'
            }

# Defining a funcitino to scrape stock prices
def get_stock_price(stock_symbol):
    #https://money.cnn.com/quote/quote.html?symb=SYMBOL_GOES_HERE
    # Example symbols: FB = Facebook, TWTR = Twitter, AAPL = Apple
    # ^ URL returns data about a given stock symbol.
    # Converting the provided stock_symbol to upper case i.e fb -> FB
    stock_symbol = stock_symbol.upper()
    URL = f"https://money.cnn.com/quote/quote.html?symb={stock_symbol}"

    # Send a get request to money.cnn.com
    response = requests.get(URL)
    # Extract the markup from the response
    markup = response.text

    # Initializing BeautifulSoup Object to traverse the Markup
    # and extract the required data
    soup = BeautifulSoup(markup, 'lxml')

    # The CNN webpage stores the latest stock price in
    # a <span/> element which is nested inside a <td/> element
    # with class 'wsod_last'. Hence we will first extract
    # the <td/> element and then extract the span element
    # nested within it.
    table_data_element = soup.find('td', class_='wsod_last')

    # Extracting the span element which contains the stock price.
    span_element = table_data_element.find('span')

    # Extracting the stock price from the span element
    # Using BeautifulSoup's text attribute.
    stock_price = span_element.text

    # Returning the stock price formatted with $ symbol
    return f"${stock_price}"


if __name__ == '__main__':
    stock_prices = {
        'facebook': get_stock_price('FB'),
        'twitter': get_stock_price('TWTR'),
        'apple': get_stock_price('AAPL')
    }

    print(
        f"\nFacebook stock is trading at {stock_prices['facebook']}"
        f"\nTwitter stock is trading at {stock_prices['twitter']}"
        f"\nApple stock is trading at {stock_prices['apple']}"    
        )