# coding=utf-8
from lxml import etree
import requests
from fake_useragent import UserAgent
import os


url1 = 'https://www.ibiquge.net/66_66791/'
url2 = 'https://www.ibiquge.net'


# 爬取HTML的函数
def get_html(url):
    ua = UserAgent()
    kv = {'user-agent': ua.random}
    re = requests.get(url, headers=kv)
    re.encoding = 'utf-8'
    htm1 = re.text
    return htm1


# 根据url获得文章并保存的函数
def get_text(url):
    html = get_html(url)
    selector = etree.HTML(html)
    title = selector.xpath('//*[@id="main"]/div/div/div[2]/h1/text()')
    txt = selector.xpath('//*[@id="content"]/text()')
    print(title)
    fp = open('txts\\' + title[0] + '.txt', 'w')
    for each in txt:
        each1 = each.replace('\ufeff', '')
        fp.write(each1.replace('\xa0', ''))
    fp.close()


def get_url(html):
    selector = etree.HTML(html)
    url_list = selector.xpath('//*[@id="list"]/dl/dd/a/@href')
    for url in url_list:
        new_url = url2 + url
        get_text(new_url)


if __name__ == '__main__':
    html = get_html(url1)
    get_url(html)



