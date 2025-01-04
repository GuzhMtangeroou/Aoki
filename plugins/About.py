from Lib import*

api = OnebotAPI.OnebotAPI()


class PluginInfo(PluginManager.PluginInfo):
    def __init__(self):
        super().__init__()
        self.NAME = "About"  # 插件名称
        self.AUTHOR = "？"  # 插件作者
        self.VERSION = "1.0"  # 插件版本
        self.DESCRIPTION = "关于"  # 插件描述
        self.HELP_MSG = "发送“*about”或“*关于”即可查看Bot信息"  # 插件帮助
        self.UID = "0bb9-fcdb-4b423f4e-52830210-8174-14f5"

def get_about(event_class, event_data: BotController.Event):
    import Lib
    if event_data.message_type == "private":  # 判断是群聊事件还是私聊事件
        BotController.send_message(f'关于\nAoki\n版本{main.VERSION}（{main.VERSION_WEEK}）\n库版本：{Lib.VERSION}（{Lib.VERSION_WEEK}）\nGithub:https://github.com/GuzhMtangeroou/Aoki/\n\n特别鸣谢\n夏柔api（https://api.aa1.cn/）\nbcmapi（https://github.com/codemaoTeam/Codemao-API）', user_id=event_data.user_id)
    else:
        BotController.send_message(QQRichText.QQRichText(f'关于\nAoki\n版本：{VERSION}（{VERSION_WEEK}）\nGithub:https://github.com/GuzhMtangeroou/Aoki/\n\n特别鸣谢\n夏柔api（https://api.aa1.cn/）\nbcmapi（https://github.com/codemaoTeam/Codemao-API）'),group_id=event_data.group_id)

EventManager.register_keyword("*关于", get_about)
EventManager.register_keyword("*about", get_about)
