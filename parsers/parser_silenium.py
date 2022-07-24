import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import time


url = 'https://adeliabonar.com/catalog'

driver = webdriver.Chrome('/chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://adeliabonar.com/catalog');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_class_name('js-product-img t-store__card__bgimg t-bgimg loaded')
#search_box.send_keys('ChromeDriver')
#search_box.submit()
#time.sleep(5) # Let the user actually see something!
#driver.quit()
print(search_box)



