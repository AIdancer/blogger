  使用pm2来创建静态文件服务器:

  # 当前目录为静态文件服务器根目录, 监听9000端口
   pm2 serve . 9000

  在本机以如下方式访问都可以(我的当前目录下有default/index.html文件):
  (10.1.1.113是我虚拟机的内网地址)

  curl http://10.1.1.113:9000/default/index.html
  curl http://localhost:9000/default/index.html

  但是在我的windows物理机上通过第一种方式就不行.

  然后查看iptables设置, 发现9000端口没有开放:

  [root@gerrylon wwwroot]# iptables -L -n
  Chain INPUT (policy ACCEPT)
  target     prot opt source               destination
  ACCEPT     all  --  0.0.0.0/0            0.0.0.0/0
  ACCEPT     all  --  0.0.0.0/0            0.0.0.0/0           state RELATED,ESTABLISHED
  ACCEPT     tcp  --  0.0.0.0/0            0.0.0.0/0           tcp dpt:22
  ACCEPT     tcp  --  0.0.0.0/0            0.0.0.0/0           tcp dpt:80
  ......

  然后使用iptables -I INPUT -p tcp --dport 9000 -j ACCEPT, 再查看:

  ACCEPT     tcp  --  anywhere             anywhere            tcp dpt:http
  [root@gerrylon wwwroot]# iptables -L -n
  Chain INPUT (policy ACCEPT)
  target     prot opt source               destination
  ACCEPT     tcp  --  0.0.0.0/0            0.0.0.0/0           tcp dpt:9000
  ACCEPT     all  --  0.0.0.0/0            0.0.0.0/0
  ACCEPT     all  --  0.0.0.0/0            0.0.0.0/0           state RELATED,ESTABLISHED
  ACCEPT     tcp  --  0.0.0.0/0            0.0.0.0/0           tcp dpt:22
  ACCEPT     tcp  --  0.0.0.0/0            0.0.0.0/0           tcp dpt:80
  ......

  再以第一种方式访问就可以了.

  上述设置在机器重启后就会失效, 要想永久生效, 可以将配置写入到/etc/sysconfig/iptables,
  然后重启iptables

  # 在/etc/sysconfig/iptables加上这句
  -A INPUT -p tcp -m tcp --dport 9000 -j ACCEPT

  # 重启iptables
  service iptables restart
