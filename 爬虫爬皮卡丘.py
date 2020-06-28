# -*- coding: utf-8 -*-
import re
import requests
import time
import os
headers = {
        'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }

url = "http://image.baidu.com/search/index?tn=baiduimage&word=美图" + "page=" + str(3)
html = requests.get(url)
html.encoding = html.apparent_encoding
html = html.text
urls = re.findall('"objURL":"(.*?)"', html, re.S)
i = 0
for url in urls:
    time.sleep(3)
    image = requests.get(url, headers=headers, timeout=6).content
    if image:
        with open('美图\\' + str(i) + '.jpg', 'wb') as f :
            print("正在下载%d的张图片：%s" % (i+1, url))
            f.write(image)
        i += 1
    else:
        print("链接超时，下载失败")
print("图片下载成功")

