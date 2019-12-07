#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 股东股本->分红配股

## http://quotes.money.163.com/f10/fhpg_000001.html#01d05

import requests
from bs4 import BeautifulSoup

url = 'http://quotes.money.163.com/f10/fhpg_000001.html#01d05'
wb_data = requests.get(url)
# print(wb_data.text)
# html = '''
# <ul>
#     <li class="item-0" name="one"><a href="www.baidu.com">baidu</a>
#     <li class="item-1" name="two"><a href="www.alibaba.com">alibaba</a>
# '''
# soup = BeautifulSoup(html,'html.parser')
# print(soup.li.a.string)
soup = BeautifulSoup(wb_data.text,"html.parser")
# print(soup)
path = '.inner_box'
soup = soup.select(path)
print(soup.select(" table"))
print(soup.count('thead'))


# print("####################################################################################")
#
# trrs = soup.select('tr')[2].select('td')
# print(trrs)
# for item in trrs:
#     print(item.text)