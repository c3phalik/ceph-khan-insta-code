"""
Author: Ceph A. Khan

Series: Using BeautifulSoup to scrap data from HTML

Description: 
Python program to demonstrate
extracting data from HTML Markup.

We will scrape Top 10 Google results in this program.

"""
from bs4 import BeautifulSoup
import requests as r

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
response = r.get('https://google.com/search?q=Python', headers=headers)
soup = BeautifulSoup(response.text, 'lxml')

results = soup.find_all('div', class_='rc')

for result in results:
    
    headline_div = result.find('div', class_='r')
    desc_div = result.find('div', class_='s')
    

    url = headline_div.find('a').get('href')
    headline = headline_div.find('h3').text
    description = desc_div.find('div').find('span').text

    print(f'Headline: {headline}\nUrl: {url}\ndesciption: {description}')