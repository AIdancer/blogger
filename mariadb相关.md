
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


### mariadb 修改root密码
    1. Open and edit /etc/my.cnf or /etc/mysql/my.cnf, depending on your distribution.
    2. Add skip-grant-tables under [mysqld]
    3. Restart MySQL
    4. You should be able to log in to MySQL now using the below command mysql -u root -p
    5. Run mysql> flush privileges;
    6. Set new password by ALTER USER 'root'@'localhost' IDENTIFIED BY 'NewPassword';
    7. Go back to /etc/my.cnf and remove/comment skip-grant-tables
    8. Restart MySQL
    9. Now you will be able to login with the new password mysql -u root -p


### 在CentOS中，可以安装MariaDB用作MYSQL的替代品。
    MariaDB数据库管理系统是MySQL的一个分支，主要由开源社区在维护，采用GPL授权许可。
    开发这个分支的原因之一是：甲骨文公司收购了MySQL后，有将MySQL闭源的潜在风险，因此社区采用分支的方式来避开这个风险。
    MariaDB的目的是完全兼容MySQL，包括API和命令行，使之能轻松成为MySQL的代替品。
    安装mariadb，大小59 M。
    yum install mariadb-server mariadb
    mariadb数据库的相关命令是：
    systemctl start mariadb  #启动MariaDB
    systemctl stop mariadb  #停止MariaDB
    systemctl restart mariadb  #重启MariaDB
    systemctl enable mariadb  #设置开机启动
    所以先启动数据库 : systemctl start mariadb
    然后就可以正常使用mysql了。
    
### 在MacOS中，可以使用brew直接安装。
    brew install mysql.
    之后需要启动mysql的服务：bash mysql.server start
    现在你就可以使用mysql了。

### C/C++开发中编译参数的获取。
    mysql_config --cflags --libs
    更详细的内容及开发示例请参照：http://zetcode.com/db/mysqlc/

