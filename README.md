# worldFriendsIT_Crawler
# 월드프렌즈it봉사단 새로운 공지사항 알려주는 봇



> 합격자발표 직접 찾아보기 번거로워 2시간전에 개발시작.



* 개발언어

> Python 3.6

* 사용 라이브러리

> python-telegram-bot
>
> requests
>
> beautifulSoup4







-------

작동원리

1. https://kiv.nia.or.kr/front/sptr_news/noticeList.do 에서 공지사항 크롤링	(cron작업)
2. 크롤링 데이터에 2018/05/17 (합격발표예상날짜) 가 들어가는지 비교
3. 맞으면 telegram bot 코드 실행 
4. 공지사항뜨면 나는 텔레그램으로 확인



> 저 합격되게 해주세요