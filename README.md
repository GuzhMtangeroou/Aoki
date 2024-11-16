![center](https://static.codemao.cn/pickduck/Hkq2gsCCA.jpg)
<h2>看板fu（bushi）</h2>
<h1 align="center">Aoki-青木</h1>
<p align="center" class="shields">
    <a href="https://github.com/GuzhMtangeroou/Aoki/issues" style="text-decoration:none">
        <img src="https://img.shields.io/github/issues/GuzhMtangeroou/Aoki.svg?style=for-the-badge" alt="GitHub issues"/>
    </a>
    <a href="https://github.com/GuzhMtangeroou/Aoki/stargazers" style="text-decoration:none" >
        <img src="https://img.shields.io/github/stars/GuzhMtangeroou/Aoki.svg?style=for-the-badge" alt="GitHub stars"/>
    </a>
    <a href="https://github.com/GuzhMtangeroou/Aoki/forks" style="text-decoration:none" >
        <img src="https://img.shields.io/github/forks/GuzhMtangeroou/Aoki.svg?style=for-the-badge" alt="GitHub forks"/>
    </a>
    <a href="https://github.com/GuzhMtangeroou/Aoki/blob/master/LICENSE" style="text-decoration:none" >
        <img src="https://img.shields.io/static/v1?label=LICENSE&message=GPL-3.0&color=lightrey&style=for-the-badge" alt="GitHub license"/>
    </a>
    <a href="https://github.com/botuniverse/onebot" style="text-decoration:none">
        <img src="https://img.shields.io/badge/OneBot-11-black?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHAAAABwCAMAAADxPgR5AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAxQTFRF////29vbr6+vAAAAk1hCcwAAAAR0Uk5T////AEAqqfQAAAKcSURBVHja7NrbctswDATQXfD//zlpO7FlmwAWIOnOtNaTM5JwDMa8E+PNFz7g3waJ24fviyDPgfhz8fHP39cBcBL9KoJbQUxjA2iYqHL3FAnvzhL4GtVNUcoSZe6eSHizBcK5LL7dBr2AUZlev1ARRHCljzRALIEog6H3U6bCIyqIZdAT0eBuJYaGiJaHSjmkYIZd+qSGWAQnIaz2OArVnX6vrItQvbhZJtVGB5qX9wKqCMkb9W7aexfCO/rwQRBzsDIsYx4AOz0nhAtWu7bqkEQBO0Pr+Ftjt5fFCUEbm0Sbgdu8WSgJ5NgH2iu46R/o1UcBXJsFusWF/QUaz3RwJMEgngfaGGdSxJkE/Yg4lOBryBiMwvAhZrVMUUvwqU7F05b5WLaUIN4M4hRocQQRnEedgsn7TZB3UCpRrIJwQfqvGwsg18EnI2uSVNC8t+0QmMXogvbPg/xk+Mnw/6kW/rraUlvqgmFreAA09xW5t0AFlHrQZ3CsgvZm0FbHNKyBmheBKIF2cCA8A600aHPmFtRB1XvMsJAiza7LpPog0UJwccKdzw8rdf8MyN2ePYF896LC5hTzdZqxb6VNXInaupARLDNBWgI8spq4T0Qb5H4vWfPmHo8OyB1ito+AysNNz0oglj1U955sjUN9d41LnrX2D/u7eRwxyOaOpfyevCWbTgDEoilsOnu7zsKhjRCsnD/QzhdkYLBLXjiK4f3UWmcx2M7PO21CKVTH84638NTplt6JIQH0ZwCNuiWAfvuLhdrcOYPVO9eW3A67l7hZtgaY9GZo9AFc6cryjoeFBIWeU+npnk/nLE0OxCHL1eQsc1IciehjpJv5mqCsjeopaH6r15/MrxNnVhu7tmcslay2gO2Z1QfcfX0JMACG41/u0RrI9QAAAABJRU5ErkJggg==" alt="Badge">
    </a>
    <br>
  
### 这是一个基于python适配onebot11协议的QQBot ~~(框架?)~~
### 首先感谢您选择/使用了青木作为您的QQBot（框架）
##### ~~作者自己写着用的，有一些写的不好的地方还请见谅（不过估计也没人会用我这个项目吧）~~

### 当前版本：1.0（2024#4）

<details>
<summary>基本目录结构</summary>

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
├─ config.yml   配置文件
├─ main.py      主程序（运行这个直接启动）
├─ app.pyw      带启动界面的主程序（运行这个也可启动）
└─ README.md    这个文件就不用解释了吧（？）

└─ README_en.md 诶你怎么似了（懒得翻译.png
```

</details>


## 部署
**作者在python3.11.4编写、测试均未发现问题，其他版本暂未测试**

### 本项目[`文档`](docs/Readme.md) 

## 版本号
* 目前版本为......看上面去
* 关于版本号与版本周的说明：
   * 版本号格式为`<主版本>.<次版本>(<年份>#<季度>-<特殊信息（如有）>` 例如`1.0（2024#3）`
   * 特殊信息一览：
   * tes:测试版本
   * tes-pu:公测版本
   * bad:存在问题/未经详细测试的版本
   * goose:诶你猜
     
     
     

## 插件
#### 一切都需要编写插件来实现功能
#### 不过我们有一些我们自己制作的插件，后续可能会放在源码中或是releases中

## ❤️鸣谢❤️
没有，别看了
