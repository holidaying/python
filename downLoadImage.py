path = "/Users/liudan/Desktop/test.jpg"
import requests
def down(url):
    try:
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
    except:
        print("异常")
