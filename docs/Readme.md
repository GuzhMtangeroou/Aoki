# Aoki·文档
#### 本文档可能并非适用于最新的代码，如遇到错误请发送issue，随缘处理吧 ~~要不你帮我中考？秒回~~
> 基于[`MuRainBo2文档`](https://github.com/xiaosuyyds/MuRainBot2/tree/master/docs)编写，本文档较原文档已发生更改，并以[`CC-BY-NC-SA`](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh-hans)协议分发
### 在这里，你将会学会：
 - 如何部署
 - 如何使用

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
**附：~~（可能是）~~正常启动的log**
```text
[2024-12-14 20:03:11,348] [main.py] [INFO]: 开始运行，当前版本：1.0(24#4)
[2024-12-14 20:03:11,856] [main.py] [INFO]: 插件导入完成，共成功导入 4 个插件:
[2024-12-14 20:03:11,857] [main.py] [INFO]: 插件导入完成，共导入 4 个插件:
[2024-12-14 20:03:11,857] [main.py] [INFO]:  - About: About by ？,UID:0964-fcdb-4b423f4e-52836a51-ef7d-ba1d
[2024-12-14 20:03:11,857] [main.py] [INFO]:  - Control: CTRL by vika,UID:0964-fcdb-4b423f4e-52836a51-ef7d-ba1d
[2024-12-14 20:03:11,857] [main.py] [INFO]:  - Helper: Helper by 你说是校溯还是vika,UID:0964-fcdb-4b423f4e-52836a51-ef7d-ba1d
[2024-12-14 20:03:11,857] [main.py] [INFO]:  - pluginTemplates: HelloWorld by You,UID:0964-fcdb-4b423f4e-52836a51-ef7d-ba1d
[2024-12-14 20:03:11,857] [main.py] [INFO]:  - Manager: Manager  by ？,UID:0964-fcdb-4b423f4e-52836a51-ef7d-ba1d
[2024-12-14 20:03:11,858] [main.py] [INFO]:  - Play: Play  by vika,UID:0964-fcdb-4b423f4e-52836a51-ef7d-ba1d
[2024-12-14 20:03:11,859] [main.py] [INFO]: 将以127.0.0.1:5801启动监听服务器
[2024-12-14 20:03:11,859] [main.py] [INFO]: 将以http://127.0.0.1:5800调用API
[2024-12-14 20:03:11,859] [main.py] [INFO]: BotUID或昵称来源：自动获取......
[2024-12-14 20:03:13,893] [OnebotAPI.py] [ERROR]: 调用 API: /get_login_info data: None 异常: ConnectionError(MaxRetryError("HTTPConnectionPool(host='127.0.0.1', port=5800): Max retries exceeded with url: /get_login_info (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000002445693BCD0>: Failed to establish a new connection: [WinError 10061] 由于目标计算机积极拒绝，无法连接。'))"))
[2024-12-14 20:03:13,894] [main.py] [ERROR]: 获取BotUID与昵称失败，可能会导致严重问题(ConnectionError(MaxRetryError("HTTPConnectionPool(host='127.0.0.1', port=5800): Max retries exceeded with url: /get_login_info (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000002445693BCD0>: Failed to establish a new connection: [WinError 10061] 由于目标计算机积极拒绝，无法连接。'))")))
[2024-12-14 20:03:13,895] [main.py] [INFO]: 欢迎使用 (None)
[2024-12-14 20:03:13,896] [main.py] [INFO]: 开启命令输入
[2024-12-14 20:03:13,896] [main.py] [INFO]: 启动监听服务器
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
有两种方法，1.使用sb.(somebody)写的小工具全自动安装(😀📕📕针👍)，2.手动安装
> 使用😀📕📕写的小工具自动安装

首先打开😀📕📕写的小工具的项目[Lagrange.Installer](https://github.com/xiaosuyyds/Lagrange.Installer)

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
### 配置
> 恭喜你，你已经成功安装Onebot实现端，接下来我们开始配置Bot吧！

首先运行(`ConfigEditior.pyw`)，欸，配置文件有点抽象怎么办？~~其实注释在这（）~~
```text
#配置文件

#账号
account: # 账号相关
  user_id:   # QQ账号（留空则自动获取）
  nick_name: "" #昵称（留空则自动获取）
  bot_admin: []

#网络
api: # Api设置
  host: '127.0.0.1'
  port: 5800

server: # 监听服务器设置
  host: '127.0.0.1'
  port: 5801

rc: # 远程连接设置
  start: false #是否开放远程连接
  host: '127.1.0.1'
  port: 5001

#启动
start_img:
  show: true #是否显示启动图
  height: 128 #启动图高
  weight: 128 #启动图宽

show_cmd:
  show: true #启动时是否显示控制台

color_word:
  show: false #启动时是否显示渐变色文字
  
#其他
thread_pool: # 线程池最大线程数
  max_workers: 5

qq_data_cache: # QQ数据缓存设置
  enable: true # 是否启用缓存
  expire_time: 300  # 缓存过期时间（秒）
  max_cache_size: 500  # 最大缓存数量（设置过大可能会导致报错）


debug: # 调试模式
  enable: false # 是否启用调试模式

auto_restart_onebot: # 在Onebot实现端状态异常时自动重启Onebot实现端（需开启心跳包）
  enable: true # 是否启用自动重启
```

您只需要在account.bot_admin中添加您自己的QQ号即可，其余的配置项暂时可以不用管他

---

> 接下来就是最后一步，运行main.py和Onebot实现了！

Onebot实现端你自己启动吧，文档都有

Bot运行命令为`python main.py`

### 至此，您已经成功安装并配置了Aoki，请尽情享用吧！
> #### 更进一步: [了解如何自行编写插件](Writing_Plugins.md)
