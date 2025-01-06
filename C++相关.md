### MinGW下载器地址
```bash
https://sourceforge.net/projects/mingw/files/
```

### vscode设置mingw编译
ctrl+shift+p，设置cpp json中的compilerPath，内容示例如下，根据gcc/g++路径修改即可   
```bash
{
  "configurations": [
    {
      "name": "windows-gcc-x64",
      "includePath": [
        "${workspaceFolder}/**"
      ],
      "compilerPath": "D:/app/msys64/mingw64/bin/gcc.exe",
      "cStandard": "${default}",
      "cppStandard": "${default}",
      "intelliSenseMode": "windows-gcc-x64",
      "compilerArgs": [
        ""
      ]
    }
  ],
  "version": 4
}
```

### 输出wstring中文
```c++
#define _CRT_SECURE_NO_WARNINGS

#include <ctime>
#include <chrono>
#include <iostream>
#include <memory>
#include <string>
#include <thread>
#include <typeinfo>
#include <vector>

#include <Windows.h>

using namespace std;

int main(int argc, char* argv[]) {
    string s1 = "我是你爸爸";
    wstring s2 = L"我是你爸爸";
    cout << s1.length() << " " << s2.length() << endl;
    setlocale(LC_ALL, "chs");
    wcout << s2 << endl;
    wcout << s2[0] << endl;
    return 0;
}
```







