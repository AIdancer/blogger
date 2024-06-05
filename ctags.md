## ctags常用命令
### 索引C/C++文件
```bash
    ctags -R -f tags_mysql --c++-kinds=+p --fields=+iaS --extras=+q /usr/include/mysql/
    ctags -R --languages=c++ --c++-kinds=+px --fields=+iaS --extras=+q --exclude=build --exclude=CMakeLists.txt `pwd`
```

### 加载tags文件
```bash
set tags=tags_file;
set tags+=another_tgas_file;
```
