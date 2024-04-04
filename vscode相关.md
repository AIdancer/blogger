### vscode配置anaconda python环境
设置.vscode setting.json配置项
```
"python.defaultInterpreterPath": "C:\\Users\\86133\\.conda\\envs\\factor\\python.exe(your python interpeter path)"
```

### VSCode远程C++添加CppIncludePath
```
{
    "files.associations": {
        "vector": "cpp",
        "ostream": "cpp",
        "chrono": "cpp"
    },
    "C_Cpp.default.includePath": [
        "${workspaceFolder}/include",
        "${workspaceFolder}/src",
        "/usr/include/mysql"
    ],
}
```
