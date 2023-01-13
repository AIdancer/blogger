
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

如何寻找静态文件
---------------
```
Create the static path whenever you want it inside your project. 
In my case I placed it in /root_folder/frontend/static for the static files 
and /root_folder/frontend/templates for my templates, 
then I passed the routes to the constructor, like this:

app = Flask(__name__, template_folder='../frontend/templates', 
static_folder='../frontend/static/')
Finally my html tag looks like this:

<link rel="stylesheet" href="../static/styles.css">
```
