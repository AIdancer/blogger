### MinGW下载器地址
```bash
https://sourceforge.net/projects/mingw/files/
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







