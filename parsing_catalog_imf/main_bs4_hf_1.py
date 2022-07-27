import requests
from bs4 import BeautifulSoup
from requests.api import head



def get_data(url):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"}
    req = requests.get(url=url, headers=headers)

    with open('parsing_catalog_imf/json_file/index2_2.json', 'w') as file:
        file.write(req.text)



url = 'https://store.tildacdn.com/api/getproductslist/?storepartuid=105150852661'
url_2 = 'https://store.tildacdn.com/api/getproductslist/?storepartuid=105150852661&recid=420874855&c=1658871063166&getparts=true&getoptions=true&slice=1&&size=100'


get_data(url_2)

