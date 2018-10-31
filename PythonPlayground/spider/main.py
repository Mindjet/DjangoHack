import os
import random
import re

import requests

os.chdir(os.path.dirname(__file__))


def get_mp4_urls():
    response = requests.get('http://www.xiaohuar.com/v/')
    urls = re.findall(r'class="items".*?src="(.*?)"', response.text, re.S)
    print(urls)
    return urls


def get_mp4_resource(mp4_url):
    response = requests.get(mp4_url)
    resource_url = re.findall(
        r'id="media".*?src="(.*?)"', response.text, re.S)[0]
    try:
        video = requests.get(resource_url, timeout=5)
    except TimeoutError:
        video = None
        print('exception')
    return video


def spider_go():
    urls = get_mp4_urls()
    # print('total count is: ' + str(len(urls)))
    # for i, url in enumerate(urls):
    #     video = get_mp4_resource(url)
    #     name = ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba', 5))
    #     fullname = name + '.mp4'
    #     with open(fullname, 'wb') as file:
    #         if video is not None:
    #             file.write(video.content)
