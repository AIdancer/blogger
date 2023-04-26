### ubuntu设置固定ip
**安装ifupdown**  
```
sudo apt install ifupdown
```
**查看本机ip配置信息**  
```
ifconfig

#比如
eno8303: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether b8:cb:29:f9:92:63  txqueuelen 1000  (以太网)
        RX packets 2010  bytes 2298038 (2.2 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 1201  bytes 144880 (144.8 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
        device interrupt 17

eno8403: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.31.92  netmask 255.255.255.0  broadcast 192.168.31.255
        inet6 fe80::5d9e:cff7:c139:4c18  prefixlen 64  scopeid 0x20<link>
        ether b8:cb:29:f9:92:64  txqueuelen 1000  (以太网)
        RX packets 1353454  bytes 1929254730 (1.9 GB)
        RX errors 0  dropped 32  overruns 0  frame 0
        TX packets 376627  bytes 29851332 (29.8 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
        device interrupt 18

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (本地环回)
        RX packets 8973  bytes 771044 (771.0 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 8973  bytes 771044 (771.0 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

```

**查看路由信息**  
```
netstat -rn

eno8303: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether b8:cb:29:f9:92:63  txqueuelen 1000  (以太网)
        RX packets 2010  bytes 2298038 (2.2 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 1201  bytes 144880 (144.8 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
        device interrupt 17

eno8403: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.31.92  netmask 255.255.255.0  broadcast 192.168.31.255
        inet6 fe80::5d9e:cff7:c139:4c18  prefixlen 64  scopeid 0x20<link>
        ether b8:cb:29:f9:92:64  txqueuelen 1000  (以太网)
        RX packets 1353454  bytes 1929254730 (1.9 GB)
        RX errors 0  dropped 32  overruns 0  frame 0
        TX packets 376627  bytes 29851332 (29.8 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
        device interrupt 18

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (本地环回)
        RX packets 8973  bytes 771044 (771.0 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 8973  bytes 771044 (771.0 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

```
