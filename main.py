import requests
from bs4 import BeautifulSoup
from requests.api import head

url = 'https://store.tildacdn.com/api/getproductslist/?storepartuid=105150852661'
headers = {
       "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
   }
# def get_articles_urls(url):
#     s = requests.Session()
#     response = s.get(url=url, headers=headers)
#
#     with open('index.html', 'w') as file:
#         file.write(response.text)
#         print(type(response.text))
#
# def main():
#     get_articles_urls(url='https://adeliabonar.com')
#
#
# if __name__=='__main__':
#     main()
#

result = requests.get(url, headers=headers).json()
#print(result)

for name in result['products']:
    title_soup = BeautifulSoup(name['title'],'lxml')
    title_soup = title_soup.find('p').text

    text_soup = BeautifulSoup(name['text'],'lxml')
    text_soup = text_soup.text

    gallery_soup = BeautifulSoup(name['gallery'],'lxml')
    gallery_soup = gallery_soup.text


    editions_soup = BeautifulSoup(str(name['editions']),'lxml')
    characteristics_soup = BeautifulSoup(str(name['characteristics']),'lxml')
    #color_soup = BeautifulSoup(name['Цвет'],'lxml')
    print(f'{title_soup}\n{text_soup}\n{gallery_soup}\n{editions_soup}\n{characteristics_soup}\n\n')




