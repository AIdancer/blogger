### 设置系统时间及时区
```bash
1.删除本地时间

rm -rf /etc/localtime
2.设置时区为上海

ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

```
