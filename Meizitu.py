import requests
from threading import Thread
import time
from lxml import etree
import os


def request_index(url):
    index_headers = dict()
    index_headers[
        'user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    
    res = requests.get(url, headers=index_headers)
    index_html = etree.HTML(res.text)
    hrefs = index_html.xpath('//*[@id="pins"]/li/a/@href')
    alts = index_html.xpath('//*[@id="pins"]/li/a/img/@alt')

    for href, alt in zip(hrefs, alts):
        src_model, photo_num = get_into_pindex(href, headers=index_headers)

        if os.path.exists('F:/Meizitu/' + alt):
            continue

        else:
            os.mkdir('F:/Meizitu/' + alt)

        thread_list = list()
        for i in range(1, int(photo_num) + 1):
            if i < 10:
                i = '0' + str(i)

            else:
                pass

            print(src_model, i)
            src = src_model % i

            thread_list.append(Thread(
                target=download_image,
                args=(src, alt, i, href)
            ))

        for i in thread_list:
            i.start()
            i.join(0.6)


def download_image(src, alt, i, href):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'referer': href
    }
    image_data = requests.get(src, headers=headers).content
    print(i)

    with open('F:/Meizitu/' + alt + '/' + alt + ' ' + str(i) + '.jpg', 'wb') as f:
        f.write(image_data)


def get_into_pindex(href, headers):
    res = requests.get(href, headers=headers)
    print(res.status_code)
    pindex_html = etree.HTML(res.text)
    src_models = pindex_html.xpath('/html/body/div[2]/div[1]/div[3]/p/a/img/@src')
    photo_nums = pindex_html.xpath('/html/body/div[2]/div[1]/div[4]/a[5]/span/text()')

    src_models = src_models[0][: -6] + '%s' + '.jpg'
    print(src_models, photo_nums)
    return src_models, photo_nums[0]


if __name__ == '__main__':
    urls = ['https://www.mzitu.com/mm/page/%s' % s for s in range(1, 100)]
    for url in urls:
        request_index(url)


