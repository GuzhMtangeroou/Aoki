## 在这一篇中，你将学会如何做你的第一个插件

#### 首先你需要对本项目的项目结构与插件系统有一个了解
> ~~😀📕📕针👍~~

目录我就不详细说了，[`readme`](../README.md)里面有

我们要说的是其中对于插件最重要的extensions与extensions_configs文件夹（自定义了插件和插件配置文件目录的论外啊喵）

 - `extensions`文件夹是用来存放插件的，里面需要放插件的源码
 - `extensions_configs`文件夹是用来存放插件的配置文件，里面需要有插件的配置文件

---

接下来我们要说的是插件系统，插件系统是非常重要的一部分 ~~（毕竟没了插件就单一个框架啥也干不了）~~

插件系统负责导入插件的部分在`Lib\ExsManager.py`中

导入完成后便会将全部成功导入的插件存在一个列表里，格式如下
```python
[{"name": "plugin's filename", "prog": plugin1}, ...] #prog:programの缩写
```

当框架收到上报时则会将上报的信息传递给插件（说白了就是执行一个函数）然后由插件自行处理

因此，插件必须写一个函数并注册到EventManager中，~~不然这插件就是个废物~~

当然也有别的方法，你可以在插件中写一个`main`函数，框架会把全部收到的上报都传递到这个函数
但是我们不推荐这样使用， 因为这会无法使用插件系统&事件系统的全部功能

---

> 好的，现在你对插件系统与事件系统有了个基本的了解，接下来就让我们开始正式的写你的第一个插件吧！
~~其实我们送了一些插件可以白嫖（api来源：https://api.aa1.cn/）~~
> 
> 这个插件需要实现在私聊与群聊中发送hello自动回复Hello World!

首先新建一个python文件在extensions文件夹下，命名为`HelloWorld.py`
> 插件尽量以大驼峰写法命名（你不用也管不了），后缀必须为`.py`

然后导入作者写~~了114514年~~的~~Sh*t hill~~SDK
```python
from Lib import *
```

接下来我们得告诉框架我们这个插件的基本信息，因此我们得定义一个类
```python
class PluginInfo:
    def __init__(self):
        self.NAME = "HelloWorld"  # 插件名称
        self.AUTHOR = "You"  # 插件作者
        self.VERSION = "1.0.0"  # 插件版本
        self.DESCRIPTION = "自动回复HelloWorld的插件"  # 插件描述
        self.HELP_MSG = ""  # 插件帮助
        self.IS_HIDDEN = False  # 插件是否隐藏（在/help命令中）
        self.UID = "（用tools/uid_maker.py生成一个）"
```

现在我们运行main.py，可以从日志种看见框架已经正确识别了你的插件

正如上文所说接下来我们需要写一个函数来接收上报

但是有两种写法，第一种是注册关键词
第二种则是注册事件

我们先写第一种也就是注册关键词
注册关键词的用法即可实现大部分功能

先写好关键词触发后执行的函数
```python
def hello_world(event_type, event_data: BotController.Event):  # 这俩参数必须得有
    if event_data.message_type == "private":  # 判断是群聊事件还是私聊事件
        # 私聊
        BotController.send_message("Hello World!", user_id=event_data.user_id)
    else:
        # 群聊
        BotController.send_message("Hello World!", user_id=event_data.user_id, group_id=event_data.group_id)
```
对于关键词注册，有两种模式
①匹配命令起始符模式
```python        
EventManager.register_start_keyword("hello", hello_world, model="EQUAL")  # 注册关键词hello，并设置为完全匹配
```
②不匹配命令起始符模式
```python        
EventManager.register_non_start_keyword("hello", hello_world, model="EQUAL")  # 注册关键词hello，并设置为完全匹配
```

第二种写法

```python
@EventManager.register_event("message")  # 注册事件名称message
def hello_world(event_class, event_data: BotController.Event):
    if event_data.message == "hello":  # 判断是群聊事件还是私聊事件
        if event_data.message_type == "private":
            BotController.send_message("Hello World!", user_id=event_data.user_id)
        else:
            BotController.send_message(QQRichText.QQRichText(QQRichText.At(event_data.user_id), "Hello World!"),
                                       group_id=event_data.group_id)
```

至此，恭喜你完成了你第一个插件的编写
~~是不是还挺简单的~~
再去试试写点别的吧 

### ***Have fun!***

> #### 更进一步: sudo rm -rf /*(bushi

~~这部分还没写，如果有实力的可以提个pr帮我写，反正随缘吧，啥时候闲的没事干写点（~~
