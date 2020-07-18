import requests
from bs4 import BeautifulSoup

url = 'https://www.daum.net/'

response = requests.get(url).text #requests의 모듈을 사용해 
                                  #get이라는 요청 방법으로 url을 text 불러와서 리스폰스에 저장

data = BeautifulSoup(response,'html.parser') #html일 경우 뷰티플소프로 읽어준다
n=0 
while n<5: 
    select = data.select_one('#wrapSearch > div.slide_favorsch > ul > li > a')
    n = n + 2
    print(select.text)

