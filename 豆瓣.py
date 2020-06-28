#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/12 下午 12:51
# @Author  : 殇夜殇雪
# @File    : 豆瓣.py
import requests
from bs4 import BeautifulSoup
headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4128.3 Safari/537.36"
}
url = "https://book.douban.com/tag/?view=type&icn=index-sorttags-all"
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "lxml")
def specific_name(tag):
    return tag.has_attr("name") and tag.get("name") == "文学"
category = soup.find(specific_name)
for e in category.next_siblings:
    if e == "\n":
        pass
    else:
        for a in e.select("a"):
            print(a.text, "https://book.douban.com" + a.get("href"))

url = "https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4"
def get_soup(url):
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "lxml")
    return soup
soup = get_soup(url)
books = {}

