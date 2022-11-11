import requests
import csv
from datetime import date
from bs4 import BeautifulSoup
from config import *

print('analyzing NFT page...')

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'}

for nft in NFTS:
    try:
        page = requests.get(nft.long_url, headers=HEADERS)
        soup = BeautifulSoup(page.content, "html.parser")

        print('retrieving data...')

        data_elements = soup.find_all(
            "section", {"class": "item--counts"}, limit=1)
        try:
            raw_views_data = data_elements[0].contents[0].contents[1].contents[0]
            raw_favorite_data = data_elements[0].contents[1].contents[1].contents[0]

            views_data = raw_views_data.split()[0]
            favorite_data = raw_favorite_data.split()[0]

            print(f'saving data to {nft.name}-analysis.csv')

            with open(f'analyses/{nft.name}-analysis.csv', 'a', encoding='UTF8', newline='') as f:
                message = MESSAGE.replace('${{SHORT_LINK}}', nft.short_url)

                writer = csv.writer(f, delimiter=',')
                writer.writerow([date.today(), QUERY, MAX_RESULT,
                                message, views_data, favorite_data])
        except:
            print('unable to scrape!! OpenSea has updated their site')
            break

    except StopIteration:
        break
