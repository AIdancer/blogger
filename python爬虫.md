### 记录点参考资料
```
https://cloud.tencent.com/developer/article/2096785
```

### 抓取财联社电报
```python
import numpy as np
import pandas as pd
import requests

if __name__ == "__main__":
    url = "https://www.cls.cn/telegraph"
    # 提取浏览器header
    header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=header)
    print(response.status_code)
    print(response.text)
    with open("log.html", "w", encoding='utf-8') as cout:
        cout.write(response.text)
```

### 爬财联社电报（筛选关键词）
```python
import datetime as dt
import logging
import json
import requests
import time
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


last_ts = None

def get_messages():
    global last_ts
    url = "https://www.cls.cn/telegraph"
    # 提取浏览器header
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=header)
    # print(response.status_code)
    # print(response.text)
    # with open("log.html", "w", encoding='utf-8') as cout:
    #     cout.write(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.title)
    res = soup.find(id="__NEXT_DATA__")
    msgs = []
    for script in res:
        data = json.loads(script)
        messages = data["props"]["initialState"]["telegraph"]["telegraphList"]
        for item in messages:
            ts = item["ctime"]
            content = item["content"]
            stock_list = item["stock_list"]
            refs = []
            for val in stock_list:
                refs.append(val["name"])
            if content.find("增") != -1:
                # print("{}   {}    {}".format(dt.datetime.fromtimestamp(ts), content, refs))
                row_data = {
                    "time" : ts,
                    "content" : content,
                    "stocks" : refs
                }
                if (last_ts is None) or (ts > last_ts):
                    msgs.append(row_data)
        break
    if len(msgs) > 0:
        last_ts = time.time()
    return msgs

if __name__ == "__main__":
    while True:
        msgs = get_messages()
        for item in msgs:
            msg = "{}      {}      {}".format(dt.datetime.fromtimestamp(item["time"]), item["content"], item["stocks"])
            print(msg)
            logger.info(msg)
        time.sleep(30)
```

### 另一个简单示例
```python
import requests
from bs4 import BeautifulSoup
url = f'https://www.fx678.com/kx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

r = requests.get(url, headers=headers)
html_content = r.text

soup = BeautifulSoup(html_content, 'html.parser')

# 查找所有class为"zb_time"的div标签
time_divs = soup.find_all('div', class_='zb_time')

# 遍历这些标签，并提取其中的文本
times = []
for div in time_divs:
    tag = div.find('a')
    if tag is not None:
        times.append(tag.text)
    else:
        print(div)

zb_word_divs = soup.find_all('div', class_='zb_word')
news = []
for div in zb_word_divs:
    news.append(div.find('a').text.strip())

pairs = soup.find_all('li', class_='body_zb_li')

date_list = {}
current_date = ""
for pair in pairs:
    date_day = pair.find('div',class_='data_time')
    if date_day is not None:
        date_list[date_day.text.strip()] = {}
        current_date = date_day.text.strip()
        continue
    else:
        times = pair.find('div',class_="zb_time").find('a')
        if times is not None:
            date_list[current_date][times.text.strip()]=pair.find('div',class_="zb_word").find('a').text.strip()

```
