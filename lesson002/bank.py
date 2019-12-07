#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request as req

url = 'http://quotes.money.163.com/f10/fhpg_000001.html#01d05'
webpage = req.urlopen(url) # 根据超链访问链接的网页

data = webpage.read() # 读取超链网页数据

data = data.decode('utf-8') # byte类型解码为字符串

print(data)
