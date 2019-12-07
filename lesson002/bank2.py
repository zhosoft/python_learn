# encoding: utf-8
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
    'Referer': 'http://quotes.money.163.com/f10/fhpg_000001.html'
}
url = 'http://quotes.money.163.com/f10/fhpg_000001.html#01d05'

response = requests.get(url, headers=headers)
text = response.text
html = etree.HTML(text)
tables = html.xpath("//table[@class = 'table_bg001 border_box limit_sale']")[1]
# trs = innerbox.xpath("//table/tbody")
trs = tables.xpath("./tbody/tr")
print(trs)

