import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
import time
from selenium import webdriver

def get_source_html(url):
    driver = webdriver.Chrome(executable_path='/chromedriver')

    driver.maximize_window()

    try:
        driver.get(url=url)
        time.sleep(3)
    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()


def main():
    get_source_html(url='https://store.tildacdn.com/api/getproductslist/?storepartuid=105150852661&recid=420874855&c=1656843108523&getparts=true&getoptions=true&slice=1&&size=100')

if __name__ == '__main__':
    main()






