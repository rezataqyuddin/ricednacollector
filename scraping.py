import requests
from bs4 import BeautifulSoup

# Configure this to be your first request URL
r = requests.get("https://funricegenes.github.io/categories/")
soup = BeautifulSoup(r.content, features='lxml')

for a_tag in soup.find_all('a', class_='listing-name', href=True):
    print('href: ', a_tag['href'])

# Configure this to the root of the above website, e.g. 'http://www.mywebsite.com'
base_url = "https://funricegenes.github.io/"

for a_tag in soup.find_all('a', class_='listing-name', href=True):
    print('-' * 60) # Add a line of dashes
    print('href: ', a_tag['href'])
    request_href = requests.get(base_url + a_tag['href'])
    print(request_href.content)