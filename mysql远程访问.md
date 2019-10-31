
#### Mariadb 10.1版本

  - 有个比较奇怪的问题，如果默认库mysql下面的user表里面存有其他root用户，那么远程访问就会失败。
  - 如果将用户删的只剩下 user = root ; host = '%' ; password = '***'的话，就可以远程访问。
  - 另外不要忘记开放iptables 3306端口
  - 最后mariadb 10.1版本 将/etc/my/cnf.d/server.cnf里面bind-address=0.0.0.0注释取消掉，便允许所有机器访问了。
  systemctl restart mariadb

