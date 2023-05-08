```
pip install jupyter
pip install ipython
```

### 修改jupyter notebook允许远程访问
```python
from notebook.auth import passwd
passwd()   #设置自己的密码，然后两次输入确认生成加密字符串


# 退出python环境，把生成的字符串复制下来，后面配置要用，然后生成jupyter配置文件，并配置：
jupyter notebook --generate-config
vim ~/.jupyter/jupyter_notebook_config.py


# 写入以下配置
c.NotebookApp.allow_remote_access = True  #允许远程访问
c.NotebookApp.allow_root = True          #允许root访问
c.NotebookApp.ip='*'                     # 所有ip皆可访问  
c.NotebookApp.password = '上面复制的那个字符串''    
c.NotebookApp.open_browser = False       # 禁止自动打开浏览器  
c.NotebookApp.port =8888                 # 端口
c.NotebookApp.notebook_dir = '设置Notebook启动进入的目录' 

# 重启jupyter
jupyter notebook

```

### 修改jupyter默认密码
    jupyter notebook password
   
### 修改jupyter默认路径
    vim 修改 ~/.jupyter/jupyter_notebook_config.py 里面 notbook_dir

### anaconda取消默认base
    conda config --set auto_activate_base false

### jupyter notebook中文和负数乱码
```
import matplotlib as mpl

mpl.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
mpl.rcParams['axes.unicode_minus']=False #用来正常显示负号
```

### pip 安装的包在jupyter中无法使用
<p>执行以下带啊吗，看当前可执行环境是那个，conda 新建的环境中可能默认并没有jupyter。</p>

```python
import sys
sys.executable
```
<p>如果确定jupyter执行环境并不在当前conda环境中，则执行一下代码用pip安装jupyter即可</p>

```python
pip install jupyter
```
