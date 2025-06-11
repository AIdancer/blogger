### 安装AB测试
```
sudo apt-get install apache2-utils
```

### ab测试post请求
```
#!/bin/bash
ab -n 10000 -c 5000 \
   -p data.json \
   -T "application/json" \
   http://localhost:8000/im_check
```
