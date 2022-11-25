### boost安装（windows）
  - 前往boost官网：https://www.boost.org/  ，下载相应版本boost库。
  - 管理员身份打开，VS自带的developer command prompt
  - b2.exe install --prefix="D:/tool/boost/x64" --build-type=complete --toolset=msvc-14.2 threading=multi --build-type=complete address-model=64
  - 上述命令中msvc-14.2注意替换成系统VS对应版本
  - complete安装编译时间大概2小时


### boost 正则
```c++
/*
1. How to use boost_regex.
   Following code is a piece of example. To compile it, you should link with "-lboost_regex -lboost_regex-mt" flag.
*/

#include <boost/regex.hpp>
#include <string>
#include <iostream>

using namespace std;

int main()
{
	const char *str = "http://www.cppprog.com/2009/0112/48.html";
	boost::cmatch mat;
	boost::regex reg( "\\d+" );
	if(boost::regex_search(str, mat, reg))
	{
		cout << mat[0] << endl;
	}
	return  0;
}
```
