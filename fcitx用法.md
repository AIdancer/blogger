### fcitx踩坑日记
```
sudo apt update
sudo apt install fcitx5 fcitx5-chinese-addons fcitx5-config-qt fcitx5-configtool

# 微信所需
sudo apt install fcitx5 fcitx5-chinese-addons \
fcitx5-configtool fcitx5-frontend-gtk3 \
fcitx5-frontend-gtk2 fcitx5-frontend-qt5 \
fcitx5-frontend-qt6
```

### 设置环境变量
```
# 微信可能不能识别fcitx5
#export GTK_IM_MODULE=fcitx5
#export QT_IM_MODULE=fcitx5
#export XMODIFIERS=@im=fcitx5

export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS=@im=fcitx
```

### 安装gnome-startup-applications
```bash
sudo apt update
sudo apt install gnome-startup-applications
```

### 添加开机自动启动项
```bash
shell中输入 gnome-session-properties 启动gnome-startup-applications，然后
打开后点「Add（添加）」：
Name：Fcitx5
Command：fcitx5 -d
Comment：随意
保存即可，下次登录自动生效。
```
