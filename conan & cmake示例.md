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
## 再来个复杂一点的
使用boost.asio的协程来处理socket
### 源代码
```c++
// 使用boost.asio的协程来处理socket
#include <boost/asio.hpp>
#include <boost/asio/awaitable.hpp>
#include <boost/asio/use_awaitable.hpp>
#include <boost/asio/experimental/awaitable_operators.hpp>
#include <fmt/core.h>
#include <iostream>
#include <string>

using namespace boost::asio;
using namespace boost::asio::experimental::awaitable_operators;
using ip::tcp;

//server side
awaitable<void> session(tcp::socket socket) {
    try {
        char data[1024];
        while (true) {
            std::size_t n = co_await socket.async_read_some(buffer(data), use_awaitable);
            std::string msg(data, n);
            std::cout << "[Server] Received: " << msg << std::endl;
            co_await async_write(socket, buffer("Echo: " + msg), use_awaitable);
        }
    } catch (std::exception& e) {
        std::cerr << "[Server] Connection closed: " << e.what() << std::endl;
    }
}

awaitable<void> server(io_context& ctx, unsigned short port) {
    tcp::acceptor acceptor(ctx, tcp::endpoint(tcp::v4(), port));
    std::cout << "[Server] Listening on port " << port << std::endl;
    while (true) {
        tcp::socket socket = co_await acceptor.async_accept(use_awaitable);
        std::cout << "[Server ] Accepted new connection" << std::endl;
        co_spawn(ctx, session(std::move(socket)), detached);
    }
}

// client side
awaitable<void> tcp_client(std::string host, unsigned short port) {
    try {
        auto executor = co_await this_coro::executor;
        tcp::resolver resolver(executor);
        tcp::socket socket(executor);

        auto endpoints = co_await resolver.async_resolve(host, std::to_string(port), use_awaitable);
        co_await async_connect(socket, endpoints, use_awaitable);
        std::cout << "[Client] Connected to " << host << ":" << port << std::endl;

        // 发送消息
        std::string message = "Hello from Client!";
        co_await async_write(socket, buffer(message), use_awaitable);

        // 接收响应
        char data[1024];
        std::size_t n = co_await socket.async_read_some(buffer(data), use_awaitable);
        std::cout << "[Client] Received: " << std::string(data, n) << std::endl;

        socket.close();
    } catch (std::exception& e) {
        std::cerr << "[Client] Error: " << e.what() << std::endl;
    }
}

int main() {
    // 使用 fmt::print 打印字符串
    fmt::print("Hello from fmt! The answer is {}.\n", 42);

    // 格式化输出
    std::string name = "Conan";
    int version = 2;
    fmt::print("Welcome to {} version {}.\n", name, version);

    io_context ctx(1);
    unsigned short port = 12345;
    // 启动服务端
    co_spawn(ctx, server(ctx, port), detached);
    // 启动客户端
    co_spawn(ctx, tcp_client("127.0.0.1", port), detached);
    ctx.run();

    return 0;
}
```
### CMakeLists.txt
```cmake
cmake_minimum_required(VERSION 3.20)
project(fmt_example CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# 让 CMake 能够找到 fmt
find_package(fmt REQUIRED)
find_package(Boost REQUIRED COMPONENTS system)

# 创建可执行文件
add_executable(app main.cpp)

target_include_directories(app PRIVATE /usr/include)

# 链接 fmt 库
target_link_libraries(app PRIVATE fmt::fmt Boost::system)
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
        self.requires("boost/1.88.0")

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
```
