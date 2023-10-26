import requests;
from bs4 import BeautifulSoup
import csv

# 爬取微博热搜榜
url = 'https://s.weibo.com/top/summary?cate=realtimehot'
response = requests.get(url)

# 解析网页内容
soup = BeautifulSoup(response.text, 'html.parser')
items = soup.find_all('tr')

# 将热搜榜信息存储到csv文件中
with open('./weibo_hot.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['排名', '热词', '热度'])
    for item in items:
        rank = item.find('td', class_='td-01').get_text().strip()
        title = item.find('td', class_='td-02').get_text().strip()
        hot = item.find('td', class_='td-03').get_text().strip()
        writer.writerow([rank, title, hot])
