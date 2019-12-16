"""
Author: Ceph A. Khan

Series: Basic web-scraping with Python

Description: 
Python program to demonstrate
the working of 'requests' module.

The requests module allows you to request
web-pages from servers.

"""

# Import the request module from Python
import requests

# Let's start with defining a method to
# request a web page.
def get_webpage(webpage_url):

    # Set headers to be sent with our request.
    # Some website detect it's absence and won't
    # serve your request.
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        # Use the get method of requests module
        # to request a web-page from google and
        # store it in a variable
        # Send the previously defined headers here
        # We can also set timeout to 
        # x seconds (optional but good practice)
        r = requests.get(webpage_url, 
                        headers=headers, 
                        timeout=5)

        # Checking if HTTP status return 200
        # HTTP 200 indicates successful request.  
        if r.status_code == 200:

            # Extracting the markup text (HTML)
            # from the response stored in variable 'r'
            webpage_markup = r.text

            # Print the markup
            print(webpage_markup)

    # Catch any possible errors and log them.
    except requests.exceptions.HTTPError as e:
        print(e)

# Testing out our program
if __name__ == '__main__':
    google = get_webpage('https://google.com')
    print(google)


