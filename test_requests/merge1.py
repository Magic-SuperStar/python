# 总结requests/bs4/pandas/beautifulsoup/
from time import sleep

import requests

user_agent = 'Mozillia/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
header = {'user-agent': user_agent}

from bs4 import BeautifulSoup as bs
import lxml.etree


# 获取电影详细信息
def get_info(i_url):
    response = requests.get(i_url, headers=header)
    # xml化处理
    resp = lxml.etree.HTML(response.text)
    # 名称
    film_name = resp.xpath('//*[@id="content"]/h1/span[1]/text()')
    # 日期
    plan_date = resp.xpath('//*[@id="info"]/span[10]/text()')
    # 评分
    rating = resp.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
    return [film_name, plan_date, rating]


def get_url_name(url):
    response = requests.get(url, headers=header)
    info = bs(response.text, 'html.parser')
    m_list = []
    for tags in info.find_all('div', attrs={'class': 'hd'}):
        for t in tags.find_all('a', ):
            iurl = t.get('href')
            m_list.append(get_info(iurl))
            print(t.find('span', ).text)
    return m_list


urls = tuple(f'https://movie.douban.com/top250?start={page * 25}&filter=' for page in range(10))

import pandas as pd

with pd.ExcelWriter(r'E:\201912\python\text.xls') as mWriter:
    m_index = 0
    for url in urls:
        m_info = get_url_name(url)
        mm = pd.DataFrame(m_info, columns=['电影名称', '上映日期', '评分'], index=range(1, 26))
        mm.to_excel(mWriter, sheet_name=f'df{m_index}')
        m_index += 1
        sleep(5)
