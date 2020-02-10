import requestTest
import re

def getHtmlText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.encoding = r.apprent_encoding
        return r.text
    except:
        return ""
    print("")

def parsePage(list,html):

    print("")

def printGoodsList(list):
    print("")

def main():

main()