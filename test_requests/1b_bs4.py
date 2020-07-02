#使用 BeautifulSoup解析网页

import requests
from bs4 import BeautifulSoup as bs
#bs4 是第三方库需要使用pip命令安装

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

header = {'user-agent':user_agent}

myurl = 'http://movie.douban.com/top250'

response = requests.get(myurl,headers=header)

bs_info = bs(response.text,'html.parser')

for tags in bs_info.find_all('div',attrs={'class':'hd'}):
    for t in tags.find_all('a',):
        print(t.get('href'))
        #获取所有链接
        print(t.find('span',).text)
        #获取电影名称