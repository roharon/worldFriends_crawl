##it

import requests
from bs4 import BeautifulSoup
import lxml

def crawl_wf():
    req = requests.get('http://kiv.nia.or.kr/front/sptr_news/noticeList.do')

    html = req.text
    #print(html)
    soup = BeautifulSoup(html,'lxml')

    #title = soup.find('td', class_='left')
    title = soup.find_all('td', class_="left")
    #print(title)

    article = []
    #print(title)
    for i in title:
        article.append(i.text)

    #print(article)
    
    try:
        if '모집 사전 공지 및 설명회 개최 안내' not in article[0]:
            print(article[0])
            return [1, article[0]]
        else:
            print("아직 안올라옴")
            return [0, article[0]]
    except:
        pass

if __name__ == '__main__':
    crawl_wf()