import Lib.ExsManager
from Lib import *

api = OnebotAPI.OnebotAPI()


class PluginInfo(ExsManager.PluginInfo):
    def __init__(self):
        super().__init__()
        self.NAME = "Helper"  # 插件名称
        self.AUTHOR = "你说是校溯还是vika"  # 插件作者
        self.VERSION = "1.0"  # 插件版本
        self.DESCRIPTION = "帮助插件"  # 插件描述
        self.HELP_MSG = "发送“*help”或“*帮助”查看帮助"  # 插件帮助
        self.IS_HIDDEN = False
        self.UID = "09c5-9ff8-11fbb2e0-a7bdd951-19b3-1253"

def get_help_text():
    plugins = Lib.ExsManager.plugins
    text = f'技能列表'
    for plugin in plugins:
        try:
            plugin_info = plugin["prog"].PluginInfo()
            if plugin_info.HELP_MSG and plugin_info.IS_HIDDEN is False:
                text += "\n{}-{}".format(plugin_info.NAME, plugin_info.HELP_MSG)
        except:
            pass
    return text


def help(event_type, event_data):
    BotController.send_message(
        QQRichText.QQRichText(
            QQRichText.Reply(event_data["message_id"]),
            get_help_text()
        ), group_id=event_data["group_id"]
    )


EventManager.register_start_keyword("帮助", help)
EventManager.register_start_keyword("help", help)
