### 教程
```bash
ip route 查看default地址是多少，该地址是wsl中本机的ip地址

host_ip=$(ip route | grep default | awk '{print $3}')
echo $host_ip 

export http_proxy="http://$host_ip:7890"
export https_proxy="http://$host_ip:7890"

curl -I https://www.google.com  # 测试代理是否有用

# 如果有异常，使用 netsh advfirewall set allprofiles state off 关闭powershell中的防火墙
# 在 Clash 设置中开启 ​​“Allow LAN”（允许局域网连接）​​。
```
