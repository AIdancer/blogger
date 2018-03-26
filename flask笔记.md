
如何设置允许外网访问请求
----------------------
    app.run(host='0.0.0.0')
    
如何让返回的json显示为中文
------------------------
```python
app.config['JSON_AS_ASCII'] = False
rt_dict = {}    
for i in range(len(content_list)):
    rt_dict[i+1] = content_list[i]['_source']['title']
return json.dumps(rt_dict, ensure_ascii=False)
```
