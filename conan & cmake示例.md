## 必须文件

### main.cpp
```c++
#include <iostream>
#include <fmt/core.h>

int main() {
    // 使用 fmt::print 打印字符串
    fmt::print("Hello from fmt! The answer is {}.\n", 42);

    // 格式化输出
    std::string name = "Conan";
    int version = 2;
    fmt::print("Welcome to {} version {}.\n", name, version);

    return 0;
}
```

### conanfile.py
```python
from conan import ConanFile
from conan.tools.cmake import cmake_layout, CMake


class ExampleRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    def requirements(self):
        self.requires("fmt/11.2.0")

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
```

### CMakeLists.txt
```
cmake_minimum_required(VERSION 3.20)
project(fmt_example CXX)

# 让 CMake 能够找到 fmt
find_package(fmt REQUIRED)

# 创建可执行文件
add_executable(app main.cpp)

# 链接 fmt 库
target_link_libraries(app PRIVATE fmt::fmt)

```

然后执行
```bash
mkdir build && cd build
conan install .. --build=missing
conan build ..
然后就安装好了, 执行./Release/app即可运行
```
或者只使用conan作为管理和下载依赖的工具, 直接用cmake编译:  
```bash
mkdir build && cd build
conan install .. --build=missing
cmake . -B build -DCMAKE_TOOLCHAIN_FILE=build/Release/generators/conan_toolchain.cmake -DCMAKE_BUILD_TYPE=Release
cmake --build build
```
