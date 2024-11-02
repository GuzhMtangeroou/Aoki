# Aoki·文档
#### 本文档可能并非适用于最新的代码，如遇到错误请发送issue，随缘处理吧 ~~要不你帮我中考？秒回~~
> 基于[`MuRainBo2文档`](https://github.com/xiaosuyyds/MuRainBot2/tree/master/docs)，本文档以[`CC-BY-NC-SA`](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh-hans)协议分发
### 在这里，你将会学会：
 - 如何部署
 - 如何使用
 - 如何使用KittenServerSDK

## 在这之前
😀📕📕针👍

## 部署
> 首先我们需要下载这个项目
1. 打开本项目的主页
2. 点击“Code”按钮
3. 点击“Download ZIP”
> 什么？你说你找不到？这是链接，直接戳这个下载吧: [我是链接](https://github.com/GuzhMtangeroou/Aoki/archive/refs/heads/master.zip)
---
> 很好，我相信你已经成功下载了这个项目，接下来开始配置~
1. 打开下载的压缩包，解压
2. 安装 [Python](https://www.python.org/downloads/)\
~~什么？你说你不会装Python？那我建议你别用了~~
3. 在终端运行 `python -m pip install -r requirements.txt`\
~~什么？你问我这个命令是干嘛的？它啊其实是用来安装本项目运行必须的依赖库的哦~~\
~~什么？你又问这个命令为什么运行不了？请检查你是否已经安装好了Python，以及你是否正确设置了环境变量，以及你是否已经将cmd/PowerShell切换到项目文件夹下~~
4. 运行 `python main.py`
> 很棒，你肯定已经成功运行了，那么此时你应该在终端内发现了几条log和一个ERROR提示，不要担心，这是正常情况，接下来我们来解决它~
**附：正常启动的log**
```text
[2024-10-06 12:26:06] [main.py] [INFO]: 当前版本：x.x(20xx#x)
[2024-10-06 12:26:06] [main.py] [INFO]: Github：https://github.com/GuzhMtangeroou/Aoki/
[2024-10-06 12:26:06] [main.py] [INFO]: 插件导入完成，共导入 4 个插件:
[2024-10-06 12:26:06] [main.py] [INFO]:  - About: About 作者:？
[2024-10-06 12:26:06] [main.py] [INFO]:  - Control: CTRL 作者:vika
[2024-10-06 12:26:06] [main.py] [INFO]:  - Helper: Helper 作者:你说是校溯还是vika
[2024-10-06 12:26:06] [main.py] [INFO]:  - pluginTemplates: HelloWorld 作者:You
[2024-10-06 12:26:06] [main.py] [INFO]: 读取到监听服务器ip，将以此ip启动监听服务器: 127.0.0.1:5841
[2024-10-06 12:26:06] [main.py] [INFO]: 读取到监听api，将以此url调用API: http://127.0.0.1:5840
[2024-10-06 12:26:06] [main.py] [INFO]: 配置文件中未找到BotUID或昵称，正在自动获取
[2024-10-06 12:26:08] [main.py] [ERROR]: 获取BotUID与昵称失败，可能会导致严重问题(ConnectionError(MaxRetryError("HTTPConnectionPool(host='127.0.0.1', port=5840): Max retries exceeded with url: /get_login_info (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x0000023096796490>: Failed to establish a new connection: [WinError 10061] 由于目标计算机积极拒绝，无法连接。'))")))
[2024-10-06 12:26:08] [main.py] [INFO]: 登录用户： (None)
[2024-10-06 12:26:08] [main.py] [INFO]: 开启命令输入
[2024-10-06 12:26:08] [main.py] [INFO]: 启动监听服务器
```
---
### 安装Onebot实现端
> 什么，你问我什么是Onebot？<br>“OneBot 标准是从原 CKYU 平台的 CQHTTP 插件接口修改而来的通用聊天机器人应用接口标准。”[你自己看吧](https://github.com/botuniverse/onebot-11/)

#### 那么，我们如何安装Onebot实现端？首先你要知道市面上的Onebot实现端有很多，目前主流的有:
- [Lagrange.Onebot](https://github.com/LagrangeDev/Lagrange.Core)
- [OpenShamrock](https://github.com/whitechi73/OpenShamrock)
- [LLOneBot](https://github.com/LLOneBot/LLOneBot)
- [NapCat](https://github.com/NapNeko/NapCatQQ)
- [~~go-cqhttp~~](https://github.com/Mrs4s/go-cqhttp)
#### 以上这些项目基本上均有详细的安装文档，请自行查看，在此我们使用Lagrange.Onebot进行示范
有两种方法，1.使用作者写的小工具全自动安装，2.手动安装
> 使用作者写的小工具自动安装

首先打开作者写的小工具的项目[Lagrange.Installer](https://github.com/xiaosuyyds/Lagrange.Installer)

然后下载[releases](https://github.com/xiaosuyyds/Lagrange.Installer/releases)内的最新版本

随后将下载的exe拖到你下载本项目的目录下，然后运行，跟随提示，完成下载及首次登陆流程

> 手动安装

自己看[Lagrange.Onebot](https://github.com/LagrangeDev/Lagrange.Core)的[文档](https://lagrangedev.github.io/Lagrange.Doc/)

然后把Lagrange.Onebot的配置文件(`appsettings.json`)中的`Implementations`字段修改为以下内容:
```json
"Implementations": [
        {
            "Type": "HttpPost",
            "Host": "127.0.0.1",
            "Port": 5841,
            "Suffix": "/",
            "HeartBeatInterval": 5000,
            "AccessToken": ""
          },
          {
            "Type": "Http",
            "Host": "127.0.0.1",
            "Port": 5840,
            "AccessToken": ""
          }
    ]
```
---
> 恭喜你，你已经成功安装Onebot实现端，接下来我们开始配置Bot吧！

首先打开配置文件(`config.yml`)

让我来为您一一介绍……个鬼啊！`config.yml`注释都这么完善了，相信你看得懂！

您只需要在account.bot_admin中添加您自己的QQ号即可，其余的配置项暂时可以不用管他

---

> 接下来就是最后一步，运行main.py和Onebot实现了！

Onebot实现端你自己启动吧，文档都有

Bot运行命令为`python main.py`

### 至此，您已经成功安装并配置了Aoki，请尽情享用吧！

## KittenServer
### （本部分仅对`with-KittenServer`分支有效）

### 背景
周知所众，编程猫源码编辑器4有个叫“海龟函数”的积木盒<br>怎么说呢，就是依托海龟编辑器客户端的KittenServer组件建立本地http服务器（127.0.0.1:8964）连接作品，执行作品传入的函数并返回值。<br>
![](https://cdn.nlark.com/yuque/0/2022/png/26472310/1647710682457-3a5a19bd-865d-483a-9d94-732b7e548497.png)
<br>于是，某个阳光明媚的下午，我在海龟编辑器的文件里发现了KittenServer的代码（）
<br>于是的于是，它就水灵灵地出现在这了（）

### 使用
在启动Bot同时启动`KittenServer.py`即可
### 注意
`KittenServer.py`需要与`main.py`在同一目录下
> #### 更进一步: [了解如何自行编写插件](plugin.md)
