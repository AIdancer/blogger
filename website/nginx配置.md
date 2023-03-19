### 下载
```
http://nginx.org/en/download.html
```

### 安装配置
```
./configure
make
sudo make install
默认安装位置为/usr/local/nginx
```

### 前端部署
```
将生成的dist文件copy到/usr/local/nginx/html
设置conf中的监听端口和index html
./nginx
./nginx -s reload (如果需要重启服务的话)
```
