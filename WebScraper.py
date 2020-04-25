
import requests
from bs4 import BeautifulSoup
#https://www.sec.gov/Archives/edgar/data
baseUrl = input('Enter Url:>')

cikNum = '/866982/'

filingsUrl = baseUrl
#basically just gathers financial data from the SEC
content = requests.get(filingsUrl)
source = content.text
file = open('gathered.txt', 'w')
file.write(str(source))
#decoded_content = content.json()
#decoded_content


