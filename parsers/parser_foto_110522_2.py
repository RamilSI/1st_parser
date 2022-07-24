import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as Bs
from urllib.parse import urljoin, urlparse
import re


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup as bs
import ssl

# # --- ignore ssl certificate ---
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
url = "https://www.weg.net/catalog/weg/RU/ru/Coatings-and-Varnishes/Liquid-Coatings/Industrial-Anticorrosive/c/TV_TL_IndustrialAnticorrosivo?h=9e722f7c"
# html = urllib.request.urlopen(url, context=ctx).read()
#
# soup = bs(html, 'html.parser')
# #media_list = soup.find_all('div', class_="col-xs-12 col-sm-6 col-lg-6")
# media_list = soup.find(attrs={"col-xs-12 col-sm-6 col-lg-6"})
#
# print(media_list)
#


session = requests.Session()
response = session.get(url, headers={'User-Agent': 'Mozilla/5.0'})

print(response)

