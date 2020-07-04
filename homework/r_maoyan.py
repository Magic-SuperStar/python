# https://maoyan.com/films?showType=3,使用requests beautifulsoup
# pandas 保存cxv文件中 utf8
import lxml
import requests
from bs4 import BeautifulSoup as bs

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
header = {}
header['user-agent'] = user_agent

main_url = 'https://maoyan.com'


def get_info(t_url):
    response = requests.get(t_url, headers=header)
    selector = lxml.etree.HTML(response.text)
    # 名字
    film_name = selector.xpath('//div[@class="movie-brief-container"]/h1/text()')
    # 类型
    film_type = selector.xpath('//div[@class="movie-brief-container"]/ul/li[1]/a/text()')
    # 日期
    plan_date = selector.xpath('//div[@class="movie-brief-container"]/ul/li[3]/text()')
    return [film_name[0], ','.join(film_type), plan_date[0]]


def get_urls(url):
    response = requests.get(url, headers=header)
    my_info = bs(response.text, 'html.parser')
    m_list = []
    for tags in my_info.find_all('div', attrs={'class': 'movie-item film-channel'})[:10]:
        t_url = tags.find('a', ).get('href')
        m_list.append(get_info(main_url + t_url))
    return m_list

import pandas as pd

my_list = get_urls('https://maoyan.com/films?showType=3')
mm = pd.DataFrame(data=my_list)
mm.to_csv('./maoyan.csv', encoding='utf8', index=False, header=False)
