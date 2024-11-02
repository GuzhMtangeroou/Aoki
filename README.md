![center](https://static.codemao.cn/pickduck/Hkq2gsCCA.jpg)
<h2>看板fu（bushi）</h2>
<h1 align="center">Aoki-青木</h1>

### 这是一个基于python适配onebot11协议的QQBot ~~(框架?)~~
### 首先感谢您选择/使用了青木作为您的QQBot（框架）
##### ~~作者自己写着用的，有一些写的不好的地方还请见谅（不过估计也没人会用我这个项目吧）~~

#### 最新版本：1.0（2024#4）

<details>
<summary>查看基本看目录结构</summary>

```
├─ data         本体及插件的临时/缓存文件
│   ├─ group  每个群的相关的缓存文件
│   │   ├─ 123  群号为123相关的缓存文件（示例）
│   │   ...
│   ├─ json     不属于某个单独群聊的Bot及插件的json临时/缓存文件
│   ...
├─ Lagrange.Core    QQBot内核框架，此处以Lagrange.Core示例
├─ Lib          Lib库，本体和插件均需要依赖此Lib
│   ├─ __init__.py     Lib
│   ├─ BotController.py   用于控制Bot
|   ├─ Configs.py      用于配置文件的一些功能
│   ├─ EventManager.py 用于广播上报事件
│   ├─ FileCacher.py   用于缓存、读取文件
│   ├─ Logger.py       用于记录日志
│   ├─ MuRainLib.py    用于提供一些零七八碎的函数
│   ├─ OnebotAPI.py    用于调用OneBotAPI
│   ├─ QQRichText.py   用于解析/处理QQ消息
│   ├─ ThreadPool.py   用于多线程（线程池）处理
│   ...
├─ logs
│   ├─ latest.log       当日的日志
│   ├─ xxxx-xx-xx.log  以往的日志
│   ...
├─ plugins
|   ├─ Control.py   核心插件（别删，删了也没啥大事）
│   ├─ xxx.py   xxx插件代码
│   ├─ yyy.py   yyy插件代码 
│   ...
├─ plugin_configs
│   ├─ pluginTemplates.py  插件模板
│   ├─ xxx.yml  xxx插件的配置文件
│   ├─ yyy.yml  yyy插件的配置文件
│   ...
├─ config.yml   MRB2配置文件
├─ main.py      MRB2代码（运行这个即可启动）
└─ README.md    这个文件就不用解释了吧（？）

└─ README_en.md 诶你怎么似了（懒得翻译.png
```

</details>


## 部署
**作者在python3.11.4编写、测试均未发现问题，其他版本暂未测试**

### 本项目[`文档`](docs/Readme.md) 

[//]: # (* 下载本项目的releases或源码包)

[//]: # (* 请下载python环境，并使用pip安装[`requirements.txt`]&#40;requirements.txt&#41;内的库)

[//]: # (* [**installer.py**]&#40;installer.py&#41;)

[//]: # (  * 运行[`installer.py`]&#40;installer.py&#41;随后静待安装成功)

[//]: # (  * 配置好之后运行先运行`Lagrange.OneBot`然后运行`main.py`即可)

[//]: # (* ~~**releases**~~)

[//]: # (  * 首先配置Lagrange.OneBot的`appsettings.json`，如有需要可以修改正反向HTTP端口)

[//]: # (  * 随后配置一下MRB2的[`config.yml`]&#40;config.yml&#41;账号和QQ号)

[//]: # (  * 配置好之后运行先运行`Lagrange.OneBot`然后运行`main.py`即可)

[//]: # (* ~~**源码包**~~)

[//]: # (  * 自行配置框架，并修改正反向HTTP端口，与框架匹配)

[//]: # (  * 随后配置一下MRB2的[`config.yml`]&#40;config.yml&#41;账号和QQ号)

[//]: # (  * 配置好之后运行先运行框架然后运行`main.py`即可)

## 版本号
* 目前版本为1.0(2024#3-tes)
* 关于版本号与版本周的说明：
   * 版本号格式为`<主版本>.<次版本>(<年份>#<季度>-<特殊信息（如有）>` 例如`1.0（2024#3）`
   * 特殊信息一览：
     tes:测试版本
     tes-pu:公测版本
     bad:存在问题/未经详细测试的版本
     goose:诶你猜

## 插件
####一切都需要编写插件来实现功能
#### 不过我们有一些我们自己制作的插件，后续可能会放在源码中或是releases中

## ❤️鸣谢❤️
没有，别看了
