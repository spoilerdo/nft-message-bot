import requests
import csv
from datetime import date
from bs4 import BeautifulSoup
from config import *

print('analyzing NFT page...')

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'}
page = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(page.content, "html.parser")

print('retrieving data...')

views_elements = soup.find_all(
    "div", {"class": "sc-29427738-0 sc-61e56300-0 cbAydH gnxLuq"}, limit=1)
raw_views_data = views_elements[0].contents[1]

favorite_elements = soup.find_all("button", {
                                  "class": "sc-b267fe84-0 cRVARX sc-29427738-0 sc-61e56300-0 cbAydH fvPiUS"}, limit=1)
raw_favorite_data = favorite_elements[0].contents[1]

views_data = raw_views_data.split()[0]
favorite_data = raw_favorite_data.split()[0]

print('saving data to analysis.csv')

with open('analysis.csv', 'a', encoding='UTF8', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow([date.today(), QUERY, MAX_RESULT,
                    MESSAGE, views_data, favorite_data])