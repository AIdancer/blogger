### 使用ssd操作git
```bash
 ssh-keygen -t ed1234 -C "your_email@example.com"
 将生成的pub内容复制到git setting的ssh key
 $ ssh -T git@github.com  测试成功后即可使用
```


### 从指定远程分支checkout一个新分支
```bash
git checkout -b master origin/master
```

### git合并master分支所有commit
```bash
# 初始化一个新的本地分支（不继承master）
git checkout --orphan latest_branch
# 添加所有文件
git add -A
# 添加commit信息
git commit -am "new version"
# 删除本地master分支
git branch -D master
# 将当前分支重命名为master分支
git branch -m master
# 用本地当前master分支覆盖远程master分支
git push -f origin master
```

#### 错误"Please move or remove them before you merge. Aborting Updating 251d632..4f9078d"
```bash
解决：
git clean -d -fx " "

参数解释：
d : 删除未被添加到git的路径中的文件
f : 强制运行
x : 删除忽略文件已经对git来说不识别的文件

注意：在执行这个命令之前，记得备份自己代码。
```
