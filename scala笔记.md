### sbt安装及问题

  brew install sbt <br>
  第一次运行sbt时速度特别慢，sbt跟maven一样需要下载很多jar包，解决方法如下：
  
 ``` bash
    1.只需要编辑 ~/.sbt/repositories文件，加入
    
    [repositories]  
    local  
    aliyun: http://maven.aliyun.com/nexus/content/groups/public/  
    central: http://repo1.maven.org/maven2/
    
    2.然后 
    sbt run  -Dsbt.override.build.repos=true
    主要是sbt后面的参数：-Dsbt.override.build.repos=true

作者：Scott Huang
链接：https://www.zhihu.com/question/31158252/answer/326757822
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
 ```
