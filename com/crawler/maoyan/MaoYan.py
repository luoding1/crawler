##爬取猫眼上面的排名前100的电影
import urllib.request
import requests
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
import json
def main():
    # crawling_movie_info()
    crawling_movie_detail()

## 爬取电影详细信息
def crawling_movie_detail():

    base_url = "http://maoyan.com"
    detail = open("detail.txt", "w", encoding="utf-8")
    with open("movie.txt", "r", encoding="utf-8") as f:
        for line in f:
            movie = json.loads(line)
            url = base_url + movie['url'];
            html = get_html(url);
            detail_info = json.dumps(parse_movie_detail(html))
            print(detail_info)
            detail.write(detail_info + "\n")
    detail.close()
    print("详细信息")

def parse_movie_detail(html):
    detail = pq(html)
    modules = list(detail(".module").items())
    introduce = pq(modules[0])(".dra").text();
    users = list(modules[1](".celebrity-group").items())
    actor = users[0](".info a").text()
    starEles = users[1](".info").items()
    stars = {}
    for user in starEles:
        key = user("a").text()
        value = user(".role").text()
        stars[key] = value.split("：")
    comments = []
    for item in modules[3](".comment-content").items():
        comments.append(item.text())

    pics = []
    for item in modules[2](".default-img").items():
        pics.append(item.attr("data-src"))

    return {
        "intruduce":introduce,
        "actor":actor,
        "stars":stars,
        "comments":comments,
        "pics":pics
    }

##爬取电影基本信息并保存在文件movie.txt文件中
def crawling_movie_info():
    count = 0;
    url = "http://maoyan.com/board/4?offset="
    with open("movie.txt", "w", encoding="utf-8") as f:
        while 2 > 1:
            current_url = url + str(count * 10)
            html = get_html(current_url)
            movies = parse_html(html)
            count = count + 1
            if len(movies) <= 0:
                print("爬虫完成")
                return
            for movie in movies:
                f.write(json.dumps(movie) + "\n")
    f.close()


#解析html 返回 解析的数据量
def parse_html(text):
    doc = pq(text)
    container = doc("#app")
    items = container(".board-wrapper dd").items()
    movies = []
    for item in items:
        movie = parse_item(item)
        movies.append(movie)
    return movies

def parse_item(item):

    image_a = item("a");
    image_url = image_a("img:last-child").attr("data-src")
    content = item(".board-item-content")
    name_dom = content(".name a")
    name = name_dom.text()
    url = name_dom.attr("href")
    movieId = parse_movie_id(name_dom.attr("data-val"))
    star = content(".star").text()
    release_time = content(".releasetime").text()
    score = content(".score").text()
    return {
        "image_url":image_url,
        "name":name,
        "url":url,
        "movieId":movieId,
        "star":star,
        "release_time": release_time,
        "score":score
    }

def parse_movie_id(movieId):
    return movieId.split(":")[1].split("}")[0]

# 获取一个页
def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }
    response = requests.get(url, headers=headers);
    return response.text
if __name__ == "__main__":
    main()