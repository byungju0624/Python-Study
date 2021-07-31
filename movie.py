from bs4 import BeautifulSoup
import urllib.request as req

code = req.urlopen("http://www.cgv.co.kr/movies/")
#print(code.read())

soup = BeautifulSoup(code, "html.parser")
#print(soup)

#내가 원하는 요소 가져오기

title = soup.select_one("strong.title")


#요소내용 가져오기
print(title.string)