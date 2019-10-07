### 外网无法访问Django
```
  让防火墙放行相应端口，以8000端口为例：
  iptables -I INPUT 4 -p tcp -m state --state NEW -m tcp --dport 8080 -j ACCEPT
  service iptables save
```
