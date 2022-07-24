import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse

def is_valid (url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

url = 'https://www.weg.net'
url_1 = 'https://waksoft.susu.ru'


def get_all_images(url):
    soup = bs(requests.get(url).content, 'html.parser')
    urls = []
    for img in tqdm(soup.find_all('jpg'), 'получено изображение'):
        img_url = img.attrs.get('src')
        if not img_url:
            continue
        img_url = urljoin(url, img_url)
        try:
            pos = img_url.index("?")
            img_url = img_url[:pos]
        except ValueError:
            pass
        if is_valid(img_url):
            urls.append(img_url)

    return urls

get_all_images(url)


