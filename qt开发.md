### QT程序打包
<p>生成的程序运行正常之后，找到项目的生成目录，比如 项目源码路径：C:\QtPros\hellomw\ 。
它的项目生成目录是 C:\QtPros\build-hellomw-Desktop_Qt_5_4_0_MinGW_32bit-Release\ 。
进入这个文件夹，在进入它的子文件夹 release 里面，找到 hellomw.exe，将这个exe 复制到一个新的单独的文件夹里用于发布，比如存到 D:\hellomw\ 文件夹里面。

然后从开始菜单打开 Qt 命令行，输入命令：cd /d D:\hellomw
然后使用 windeployqt 工具命令：windeployqt hellomw.exe
然后可以在 D:\hellomw 文件夹里看到 windeployqt 工具自动复制的插件文件夹和 dll文件、qm文件。这时候得到的就完整的 exe 程序发布集合，依赖关系都解决好了。
把 D:\hellomw 文件夹 打包就可以发布了，不用自己一个个找 dll 文件了。D:\hellomw 文件夹里的qm文件是多国语言翻译文件，不需要可以删了，其他的都保留。</p>
