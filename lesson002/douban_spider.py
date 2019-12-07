# encoding: utf-8

import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
    'Referer': 'https://movie.douban.com/'
}
url = 'https://movie.douban.com/cinema/nowplaying/shanghai/'
response = requests.get(url, headers=headers)
text = response.text
html = etree.HTML(text)
# div = html.xpath("//div[@class='mod-hd']")[1]
ul = html.xpath("//ul[@class='lists']")[0]
lis = ul.xpath("./li")
# print(ul)
movies = []
for li in lis:
    # print(etree.tostring(li,encoding='utf-8').decode('utf-8'))
    title = li.xpath("@data-title")[0]
    score = li.xpath("@data-score")[0]
    star = li.xpath("@data-star")[0]
    release = li.xpath("@data-release")[0]
    region = li.xpath("@data-region")[0]
    director = li.xpath("@data-director")[0]
    actors = li.xpath("@data-actors")[0]
    thumbnail = li.xpath(".//img/@src")[0]
    detailurl = li.xpath(".//a/@href")[0]
    movie = {
        "title": title,
        "score": score,
        "star": star,
        "release": release,
        "region": region,
        "director": director,
        "actors": actors,
        "thumbnail": thumbnail,
        "detailurl": detailurl
    }
    movies.append(movie)


print(movies)