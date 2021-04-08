```
pip install jupyter
pip install ipython
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
