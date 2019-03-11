## 百词斩个人数据导出

仅限安卓。。。

1. 手机目录`/Sdcard/Android/data/com.jiongji.andriod.card/files`，把这个文件打包发送至PC端
2. 把`read_zpk.py`放入`files`目录下，观察`files`目录下有若干个db文件，一些note在代码中，无加密，sqlite直接处理
3. 为保证个人信息安全。。仅留文件夹和文件名参考，百词斩数据存放位置，并且删除一些无用文件。
4. `zpack`文件夹下存放单词书的资源文件，序号对应单词书的序号，可在db数据库中找到。每个单词书序号下又有若干个序号文件，分别存放单词zpk文件，一个单词对应的一个zpk，关于提取方法请参考`read_zpk.py`的`read_zpk`函数