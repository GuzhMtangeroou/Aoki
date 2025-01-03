import Lib.PluginManager
from Lib import *


class PluginInfo(PluginManager.PluginInfo):
    def __init__(self):
        super().__init__()
        self.NAME = "Helper"  # 插件名称
        self.AUTHOR = "你说是校溯还是vika"  # 插件作者
        self.VERSION = "1.0"  # 插件版本
        self.DESCRIPTION = "帮助插件"  # 插件描述
        self.HELP_MSG = "发送“*help”或“*帮助”查看帮助"
        self.IS_HIDDEN = False
        self.UID = "0964-fcdb-4b423f4e-52836a51-ef7d-ba1d"  # 插件帮助


def get_help_text():
    plugins = Lib.PluginManager.plugins
    text = f'技能列表'
    for plugin in plugins:
        try:
            plugin_info = plugin["plugin"].PluginInfo()
            if plugin_info.DESCRIPTION and plugin_info.IS_HIDDEN is False:
                text += f"\n{plugin_info.NAME} - {plugin_info.DESCRIPTION}"
        # except Exception as e:
        except:
            # print(repr(e))
            pass
    text += "\n----------\n发送/help <插件名>或/帮助 <插件名>以获取插件详细帮助信息"
    return text


def help(event_type, event_data):
    if event_data.message == "/帮助" or event_data.message == "/help":
        BotController.send_message(
            QQRichText.QQRichText(
                QQRichText.Reply(event_data["message_id"]),
                get_help_text()
            ), group_id=event_data["group_id"]
        )
    else:
        plugin_name = str(event_data.message).split(" ", 1)[1].lower()
        for plugin in Lib.PluginManager.plugins:
            try:
                plugin_info = plugin["plugin"].PluginInfo()
                if plugin_info.NAME.lower() == plugin_name and plugin_info.IS_HIDDEN is False:
                    BotController.send_message(
                        QQRichText.QQRichText(
                            QQRichText.Reply(event_data["message_id"]),
                            plugin_info.HELP_MSG + "\n----------\n发送/help以获取全部的插件帮助信息"
                        ), group_id=event_data["group_id"]
                    )
                    return
            except:
                pass
        else:
            BotController.send_message(
                QQRichText.QQRichText(
                    QQRichText.Reply(event_data["message_id"]),
                    "没有找到此插件，请检查是否有拼写错误"
                ), group_id=event_data["group_id"]
            )


EventManager.register_keyword("*帮助", help)
EventManager.register_keyword("*help", help)
