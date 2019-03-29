

# KIV 월드프렌즈IT봉사단 공지사항 알림봇

![](https://img.shields.io/badge/License-MIT-blue.svg) ![](https://img.shields.io/badge/Python-3.6-blue.svg) ![](https://img.shields.io/badge/Library-bs4-green.svg) ![](https://img.shields.io/badge/Korea-KIV-mint.svg)



[t.me/KIV_alert_bot](tg://resolve?domain=KIV_alert_bot)

KIV 월드프렌즈 IT봉사단 공지사항을 알림으로 보내주는 텔레그램 봇입니다.



**다음과 같은 경우에 사용하기 편합니다**

> 언제 올라올지 모르는 KIV 단원 합격 발표 공지를 확인할때

> 해외파견 기간동안 KIV 공지사항을 확인할때



[KIV월드프렌즈IT봉사단](http://kiv.nia.or.kr/front/sptr_news/noticeList.do) 내용을 크롤링하여 정보를 제공합니다



텔레그램 봇 생성관련 URL https://core.telegram.org/bots



### Environment

* Ubuntu 16.04
* Python 3.6
* crontab 사용

### Library

* python-telegram-bot
* requests
* beautifulSoup4





```bash
python bot_Send.py

==crontab==
0 0 0 0 0 ~~/bot_Send.py

"""
제목을 기준으로 최신 글을 크롤링하는 소스입니다.
(페이지구조가 변경되어 제목을 통해 크롤링 하고 있습니다)
crawl.py 의 Line 26 의 ` '모집 사전 공지 및 설명회 개최 안내' 내용 변경을 통해 사용가능합니다.
"""
```





### 미리보기

![](https://github.com/roharon/worldFriends_crawl/blob/master/preview/KIV%20alert%20preview.PNG?raw=true)
![image](https://user-images.githubusercontent.com/4939738/55229400-3883a380-5260-11e9-8fc0-391d780fd0e9.png)





> 2018년도 방글라데시 Dhaka지역 City University 기관으로 다녀온 ITigers팀 단원입니다 
>
> 방글라데시로 가는 다른 KIV 단원분들에게 많은 도움이 되길 바라고자 [노아론 블로그](https://blog.aaronroh.org) 에 기록을 남겼습니다
>
> 기관 내 봉사 내용보다는 현지 생활 내용에 집중하여 작성하였기에 
>
> 단원분들의 현지 생활에 많은 도움이 되리라 생각합니다 (유심부터 먹거리까지)
>
>
>
> **2019년 KIV파견도 도전!**
