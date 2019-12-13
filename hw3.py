# 과제 :  순위 / 곡 제목 / 가수 (네이버영화 실습과 동일하게 저장) 1~50

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient           # pymongo를 임포트 하기
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아감
db = client.sccHomework                    # sccHomework라는 이름의 db를 만듦

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20190908',headers=headers)


soup = BeautifulSoup(data.text, 'html.parser')
# print(soup) #띄어쓰기가 제거된 html

# songList = soup.select('tbody')

titleList = soup.select('tbody > tr.list > td.check > input.select-check')
artistList = soup.select('tbody > tr.list > td.info >a.artist.ellipsis')

for j in range(50):
    print(j)
    title = titleList[j]['title']
    artist = artistList[j].text
    doc = {
        'rank' : j+1,
        'title' : title,
        'artist' : artist
    }
    db.songList.insert_one(doc)

