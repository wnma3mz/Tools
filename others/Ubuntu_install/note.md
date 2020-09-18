# Note

## 更改默认浏览器

sudo vim /usr/bin/x-www-browser

## 更改系统更新源

```bash
# 备份原有文件
cp /etc/apt/source.list /etc/apt/source.list.bak
vim /etc/apt/source.list

# 添加下面内容
# deb cdrom:[Ubuntu 16.04 LTS _Xenial Xerus_ - Release amd64 (20160420.1)]/ xenial main restricted
deb-src http://archive.ubuntu.com/ubuntu xenial main restricted #Added by software-properties
deb http://mirrors.aliyun.com/ubuntu/ xenial main restricted
deb-src http://mirrors.aliyun.com/ubuntu/ xenial main restricted multiverse universe #Added by software-properties
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted multiverse universe #Added by software-properties
deb http://mirrors.aliyun.com/ubuntu/ xenial universe
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates universe
deb http://mirrors.aliyun.com/ubuntu/ xenial multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse #Added by software-properties
deb http://archive.canonical.com/ubuntu xenial partner
deb-src http://archive.canonical.com/ubuntu xenial partner
deb http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted multiverse universe #Added by software-properties
deb http://mirrors.aliyun.com/ubuntu/ xenial-security universe

deb http://cn.archive.ubuntu.com/ubuntu/ artful main restricted universe multiverse
deb-src http://cn.archive.ubuntu.com/ubuntu/ artful main restricted universe multiverse #Added by software-properties
deb http://mirrors.aliyun.com/ubuntu/ xenial-security multiverse
# deb-src http://typora.io linux/
# 保存退出之后

sudo apt update
sudo apt upgrade
```

## 安装软件

```bash
# 常用工具
sudo apt install vim mplayer mysql-server tree git ssh ipython python-pip python3-pip

# markdown编辑工具--typora，没有翻墙可能会很慢。。。。
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys BA300B7755AFCFAE
sudo add-apt-repository 'deb http://typora.io linux/'
sudo apt-get update
sudo apt-get install typora

# shell--zsh
sudo apt install zsh
wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh
# 切换到zsh，进行配置
chsh -s /usr/local/bin/zsh
# 这里是配置文件
vim ~/.zshrc
# 找到这一行，进行修改
export ZSH=$HOME/.oh-my-zsh
# 检查下默认终端是否为zsh
vim /etc/passwd
# 找到root和当前用户名,进行如下修改，注意username替换为当前用户名
root:x:0:0:root:/root:/usr/bin/zsh
username:x:1000:1000:username,,,:/home/username:/bin/zsh

# 安装WPS
# 卸载自带的
sudo apt remove --purge libreoffice*
# 安装deb包
sudo dpkg -i libpng*.deb
sudo dpkg -i wps*.deb
# 复制字体包
cp -r wps_symbol_fonts /usr/share/fonts/

# 安装Anaconda3
# 记得修改路径/opt/anaconda3
sh Anaconda*.sh
# 安装Chrome
sudo dpkg -i google-chrome*.deb
# 解压sublime，官网下载，记得解压之后移动位置
sudo tar -xvf sublime*.tar.bz2
# 安装网易云音乐
sudo dpkg -i netease*.deb

# 设定软链接，使用绝对路径
ln -s /opt/anaconda3/bin/spyder3 /usr/bin/
ln -s /opt/anaconda3/bin/jupyter-notebook /usr/bin/
ln -s /opt/anaconda3/bin/conda /usr/bin/

# 设定pip源
# 自带的
mkdir ~/.pip
vim ~/.pip/pip.conf
# 写入下面内容
[global]
timeout = 60
index-url = https://pypi.doubanio.com/simple
# conda的
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --set show_channel_urls yes

# 安装python第三方库
sudo pip3 install numpy virtualenv bs4 requests
# 进入root再使用cond安装
conda install keras

# 安装mycli
sudo pip3 install mycli
```

## 触摸板失灵

```shell
sudo modprobe -r psmouse

sudo modprobe psmouse proto=imps
```

## 解决`home`目录下中文问题

```shell
# 全部用mv重命名成英文。。。。。。
# 然后修改配置文件
sudo vim ~/.config/user-dirs.dirs
# 将中文全部替换为对应英文即可
```

## 安装shadowsocks

```shell
sudo add-apt-repository ppa:hzwhuang/ss-qt5
sudo apt-get update
sudo apt-get install shadowsocks-qt5
```

## 制作桌面图标

```shell

# desktop
mv desktop/* /usr/share/applications
```

## 更改一些配置

#### matplotlib中文编码问题

​	[matplotlib解决中文编码的终极方案](http://blog.csdn.net/wnma3mz/article/details/77595572)

## 绑定帐号

- 网易云帐号
- github帐号
- chrome帐号（如果可以的话）

## 一些问题的解决方案

```python
/usr/share/code/bin/../code: error while loading shared libraries: libgconf-2.so.4: cannot open shared object file: No such file or directory 
```

`sudo apt install gconf2`
