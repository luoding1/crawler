import urllib.request
import requests
import urllib.parse
from urllib.robotparser import RobotFileParser
from selenium import webdriver
import re
from lxml import etree
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
def main():
    fun9();

def fun9():
    doc = pq(url="http://cuiqingcai.com")
    print(doc('title'))

def fun8():
    text = """
            <html><head><title>The Dormouse's story</title></head>
            <body>
            <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
            <p class="story">Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
            and they lived at the bottom of a well.</p>
            <p class="story">...</p>
           """
    soup = BeautifulSoup(text, 'lxml')
    print(soup.prettify())
    print(soup.title.string)


def fun7():
    text = '''
    <div>
        <ul>
             <li class="item-0 li"><a href="link1.html">first item</a>hello</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-inactive"><a href="link3.html">third item</a></li>
             <li class="item-1"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a>
         </ul>
     </div>
    '''
    html = etree.HTML(text)
    result = etree.tostring(html)
    print(result.decode('utf-8'))
    result = html.xpath('//*')
    print(result)

    html = etree.HTML(text);
    result = html.xpath('//a[@href="link1.html"]/../@class')
    print(result)
    print(html.xpath('//a[@href="link1.html"]/../text()'))
    result = html.xpath('//li[contains(@class,"li")]/a/text()')
    print(result)


def fun6():
    rp = RobotFileParser()
    rp.set_url('http://www.baidu.com/robots.txt')
    rp.read()
    print(rp.can_fetch('*', 'http://www.baidu.com/p/b67554025d7d'))


def fun5():
    browser = webdriver.Chrome()
    # browser = webdriver.Firefox()
    # browser = webdriver.PhantomJS()
    browser.get('https://www.baidu.com')
    # print(browser.current_url)


def fun4():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    r = requests.get("https://www.zhihu.com/explore", headers=headers)
    pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
    titles = re.findall(pattern, r.text)
    print(titles)


def fun1():
    print("hello luoding");
    response = urllib.request.urlopen("http://www.baidu.com");
    print(response.read());


def fun3():
    response = requests.get("http://www.baidu.com");
    print(response.text);
    print(response.headers)


def fun2():
    values = {"username": "2532511327@qq.com", "password": "ld@199210"};
    data = bytes(urllib.parse.urlencode(values), encoding="utf-8");
    print(data);
    url = "https://passport.csdn.net/account/login?" + urllib.parse.urlencode(values);
    # request = urllib.request.Request(url,data);
    response = urllib.request.urlopen(url);
    print(response.read());


if __name__ == "__main__":
    main();
