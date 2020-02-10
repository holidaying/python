import requests
from bs4 import BeautifulSoup
def getHtml(url):
    try:
        r = requests.get(url)
        r.encoding = r.apparent_encoding
        if r.status_code != 200:
            raise Exception("Invalid level!")
        soup = BeautifulSoup(r.text,"html.parser")
        print(soup.title.text)
        with open("./test.html","w") as f:
            f.write(soup)
            f.closed()
    except Exception:
        print("异常")

getHtml("http://www.baidu.com")
