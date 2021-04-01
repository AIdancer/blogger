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
