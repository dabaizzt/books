# 在写整个项目的过程中，遇到的问题，进度，新的知识

## Python2 VS Python3
- 安装python3
- 安装pip3 : apt-get install python3-pip

## 命名规则（PEP8）
- 大写字母开头的:一般是类
- 小写字母开头的: 一般是方法或者变量或者库、模块
- 方法尽量用蛇形命名法: get_books_infos() get-books_infos

## virtualenv
- 为什么使用virtualenv
- 怎么安装virtualenv: pip3 install virtualenv
- 怎么使用virtualenv: virtualenv -p pythons yourEnvName; source /yourEnvName/bin/activate; deactive

## pip list
- 查k看 pip 都安装了哪些东西

## 你如何使用 git 上拉下来的 python 项目
- 在你自己的电脑上创建一个虚拟的环境
- 进入你自己的虚拟环境
- pip install -r requirements.txt

