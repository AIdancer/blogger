### ubuntu安装es
文档:https://www.elastic.co/guide/en/elasticsearch/reference/current/deb.html

```bash
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo gpg --dearmor -o /usr/share/keyrings/elasticsearch-keyring.gpg

sudo apt-get install apt-transport-https
echo "deb [signed-by=/usr/share/keyrings/elasticsearch-keyring.gpg] https://artifacts.elastic.co/packages/8.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-8.x.list

sudo apt-get update && sudo apt-get install elasticsearch

export ELASTIC_PASSWORD="your_password"

sudo /bin/systemctl daemon-reload
sudo /bin/systemctl enable elasticsearch.service

sudo systemctl start elasticsearch.service
sudo systemctl stop elasticsearch.service

```

### 关于中文查询
ES会默认对中文的每个字符进行分词，因此中文查询时需要使用bool + must + term

### 添加数据Demo
```python
import datetime as dt
import elasticsearch.helpers
from elasticsearch import Elasticsearch

tags = {
    "600036.SH" : "银行 龙头 零售业务",
    "600862.SH" : "军工 龙头 航空材料 飞机",
    "002475.SZ" : "代工 电子 果链 科技",
    "002415.SH" : "监控 科技 视觉 AI",
    "601865.SH" : "光伏 玻璃"
}

if __name__ == "__main__":
    es = Elasticsearch("http://192.168.31.91:9200")
    package = []
    for key in tags:
        row = {
            "@timestamp" : dt.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
            "instrument" : key,
            "tag" : tags[key]
        }
        package.append(row)
    actions = [
        {
            "_index" : "stocks_tag",
            "_source" : d
        }
        for d in package
    ]
    elasticsearch.helpers.bulk(es, actions)
```

### 检索数据demo
```python
import datetime as dt
import elasticsearch.helpers
from elasticsearch import Elasticsearch

if __name__ == "__main__":
    es = Elasticsearch("http://192.168.31.91:9200")
    body = {
        "query" : {
            "bool" : {
                "must" : [
                    {
                        "term" : {
                            "tag" : "科"
                        }
                    },
                    {
                        "term" : {
                            "tag" : "技"
                        }
                    }
                ]
            }
        }
    }
    # body = {
    #     "query" : {
    #         "match_all" : {}
    #     }
    # }
    res = es.search(index="stocks_tag", body=body)
    print(res)
```

### 删除数据demo
```python
import datetime as dt
import elasticsearch.helpers
from elasticsearch import Elasticsearch

if __name__ == "__main__":
    es = Elasticsearch("http://192.168.31.91:9200")
    query = {
        "query" : {
            "match_all" : {}
        }
    }
    es.delete_by_query(index="stocks_tag", body=query)
```
