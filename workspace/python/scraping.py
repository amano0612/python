import requests
from bs4 import BeautifulSoup

#webページを取得して解析
load_url="https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content,"html.parser")

#print(soup.find("title").text)
#print(soup.find("h2").text)
#print(soup.find("li").text)

#topicを検索
#topic = soup.find(class_="topicsList_main")

#chap2の中のliタグ全て表示
for element in soup.find_all("a"):
    print(element.text)
    url = element.a.get("herf")
    print(url)

#fileName = "download.txt"
#with open(fileName,mode="w") as f:
#    f.write(response.text)