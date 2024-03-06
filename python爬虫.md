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
