import requests
from bs4 import BeautifulSoup
import lxml

def crawl_wf():
    req = requests.get('http://kiv.nia.or.kr/front/sptr_news/noticeList.do')

    html = req.text
    #print(html)
    soup = BeautifulSoup(html,'lxml')

    title = soup.find_all('tr', class_='top')
    #print(title)

    article = []
    for i in title:
        article.append(i.text)

    print(article)

    if '2019/03/27' not in article[0]:
        return [1,article[0]]
    else:
        [0,'']


if __name__ == '__main__':
    crawl_wf()
