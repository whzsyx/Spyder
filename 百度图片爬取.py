# -*- coding: utf-8 -*-


import requests
import re
import os
import random
import time

i = 0


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    try:
        html = requests.get(url, headers=headers)
        html.encoding = html.apparent_encoding  # 防止乱码，不一定所有网站都是utf-8
        if html.status_code == 200:
            print('成功获取源代码')
            # print(html.text)#这里是为了防止有些网站反爬虫，返回的值虽然是200但是源码已经不是原来的了
    except Exception as e:
        print('抓取源代码失败:%s' % e)

    return html.text


def parse_html(html):
    urls = re.findall('"objURL":"(.*?)"', html, re.S)  # 在真正的源代码上查找一下objurl
    return urls


def downloadimg(urls, name):
    global i  # 引用全局变量
    for url in urls:
        time.sleep(random.randint(1, 3))  # （1，3）代表1或者2这两个整数
        imag = requests.get(url, timeout=6).content
        if imag:
            with open("图片\\"+str(i) + '.jpg', 'wb') as f:
                print('正在下载第 %d 张图片：%s' % (i + 1, url))
                f.write(imag)
            i += 1
        else:
            print('链接超时，图片下载失败')
    print('图片下载成功')


if __name__ == '__main__':

    word = input('请您输入您需要下载图片的关键字：')
    start = int(input("请输入起始页面:"))
    end = int(input("请输入终止页面:"))
    for page in (start, end + 1):
        url = 'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=' + word + "page=" + str(
            page)
        try:
            html = get_html(url)
            imgurls = parse_html(html)
            downloadimg(imgurls, word)
        except:
            print("Wrong!")
