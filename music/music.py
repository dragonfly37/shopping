import requests
from bs4 import BeautifulSoup
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

musics = soup.select('.list-wrap > tbody > tr ')

for music in musics:
    # music 안에 a 가 있으면,
    myShow = music.select_one('tr.list > .info')

    if myShow is not None:
        myTitle = music.select_one('a.title ellipsis').text
        mySinger = music.select_one('a.artist.ellipsis').text

        print(myTitle,mySinger)