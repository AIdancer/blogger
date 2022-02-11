#### 错误"Please move or remove them before you merge. Aborting Updating 251d632..4f9078d"
```bash
解决：
git clean -d -fx " "

参数解释：

d ：删除未被添加到git的路径中的文件

f ：强制运行

x ：删除忽略文件已经对git来说不识别的文件
```
