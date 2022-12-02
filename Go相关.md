### VSCode安装go相关插件失败问题
安装完go环境之后，命令行做如下设置即可。  

```
go env -w GO111MODULE=on
go env -w GOPROXY=https://goproxy.io,direct
```
