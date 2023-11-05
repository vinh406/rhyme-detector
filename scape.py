import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://rhymer.com/'

word = "cat"

# Send a GET request to the URL
response = requests.get(url + word + '.html')

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the div element with the class attribute set to 'rhymes'
rhyme_list = soup.find_all('div', attrs={'class': 'rhymes'})

# Print the first 5 one-syllable rhyming words
for rhyme in rhyme_list[0].find_all('a')[:5]:
    print(rhyme.text)

# Print the first 5 two-syllable rhyming words
for rhyme in rhyme_list[1].find_all('a')[:5]:
    print(rhyme.text)