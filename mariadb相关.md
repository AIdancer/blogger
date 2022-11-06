
### 查看数据库物理文件路径
```
show global variables like "%datadir%"
```

### 数据文件迁移
```
centos7下，mysql默认数据目录在/var/lib/mysql. 假设我们要将该目录迁移到/data/mysql，命令如下：

cp -rp /var/lib/mysql/* /data/mysql
rsync -av /var/lib/mysql/* /data/mysql

修改 /etc/my.cnf
[mysqld]
datadir=/data/mysql
socket=/data/mysql/mysql.sock
!includedir /etc/my.cnf.d

修改 /etc/my.cnf.d/client.cnf
[client]
socket=/data/mysql/mysql.sock
port=3306

修改 /etc/my.cnf.d/server.cnf
[mysqld]
datadir=/data/mysql
socket=/data/mysql/mysql.sock

如果Centos7开启了selinux，可能会出现selinux阻止mysql访问新目录的问题，这个时候可以使用setenforce 0 临时关闭selinux看看是否是selinux的问题。
如果是被selinux阻挡的，那么输入命令：chcon -R -t mysqld_db_t /home/mysql（mysql数据文件目录位置）即可。

systemctl restart mariadb，就会发现mysql又正常了。
```

### 远程访问
```
Mariadb 10.1版本
有个比较奇怪的问题，如果默认库mysql下面的user表里面存有其他root用户，那么远程访问就会失败。
如果将用户删的只剩下 user = root ; host = '%' ; password = '***'的话，就可以远程访问。
另外不要忘记开放iptables 3306端口
最后mariadb 10.1版本 将/etc/my/cnf.d/server.cnf里面bind-address=0.0.0.0注释取消掉，便允许所有机器访问了。 systemctl restart mariadb
```
