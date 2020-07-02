# 翻页
import requests
from bs4 import BeautifulSoup as bs


# bs4是第三方库需要使用pip 命令安装

# Python 使用def定义函数，url是函数的参数
def get_url_name(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {'user-agent': user_agent}
    response = requests.get(url, headers=header)
    info = bs(response.text, 'html.parser')
    for tags in info.find_all('div', attrs={'class': 'hd'}):
        for t in tags.find_all('a', ):
            # 获取所有链接
            print(t.get('href'))
            # 获取电影名字
            print(t.find('span', ).text)


# 生成包含所有页面的元组
urls = tuple(f'http://movie.douban.com/top250?start={page * 25}&filter=' for page in range(10))

print(urls)

# 控制请求的频率，引入了time模块
from time import sleep

sleep(10)
for url in urls:
    get_url_name(url)
    sleep(5)
