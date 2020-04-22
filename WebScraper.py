import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = input('Enter URL:>')


response = requests.get(url)


soup = BeautifulSoup(response.text, "html.parser")


for one_a_tag in soup.findAll('a'):
        link = one_a_tag['href']
        download_url = url + link
        urllib.request.urlretrieve(download_url,'./'+link[link.find('filename')+1:])
        time.sleep(1)
