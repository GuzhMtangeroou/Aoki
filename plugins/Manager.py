from Lib import *
import json

api = OnebotAPI.OnebotAPI()
floodcheck=[]

class PluginInfo(PluginManager.PluginInfo):
    def __init__(self):
        super().__init__()
        self.NAME = "Manager"  # 插件名称
        self.AUTHOR = "？"  # 插件作者
        self.VERSION = "1.0"  # 插件版本
        self.DESCRIPTION = "群管理功能"  # 插件描述
        self.HELP_MSG = "666"  # 插件帮助
        self.IS_HIDDEN = True
        self.UID = "0964-fcdb-4b423f4e-52836a51-ef7d-ba1d"
    
def ban(event_class, event_data: BotController.Event):
    check=BotController.api.get_group_member_info(group_id=event_data.group_id,user_id=event_data.user_id)
    if check == "owner" or check == "admin" or event_data.user_id in Configs.GlobalConfig().bot_admin:
        message_parts = str(event_data.message).split(" ")
        if message_parts[1] == "全部" or message_parts[1] == "all":
            BotController.api.set_group_whole_ban(group_id=event_data.group_id, enable=True)
        elif len(message_parts) >= 3 and message_parts[1].isdigit() and message_parts[2].isdigit():
            BotController.api.set_group_ban(group_id=event_data.group_id, user_id=message_parts[1], duration=int(message_parts[2]))
        else:
            BotController.send_message("命令格式错误", group_id=event_data.group_id)
    else:
        BotController.send_message("以不允许的权限做了一个需要管理员权限的尝试", group_id=event_data.group_id)

def out_ban(event_class, event_data: BotController.Event):
    check=BotController.api.get_group_member_info(group_id=event_data.group_id,user_id=event_data.user_id)
    if check == "owner" or check == "admin" or event_data.user_id in Configs.GlobalConfig().bot_admin:
            message_parts = str(event_data.message).split(" ")
            if message_parts[1] == "全部" or message_parts[1] == "all":
                BotController.api.set_group_whole_ban(group_id=event_data.group_id, enable=True)
            elif len(message_parts) >= 3 and message_parts[1].isdigit() and message_parts[2].isdigit():
                BotController.send_message("单人禁言暂时无法解除", group_id=event_data.user_id)
    else:
        BotController.send_message("以不允许的权限做了一个需要管理员权限的尝试", group_id=event_data.group_id)

def helps(event_class, event_data: BotController.Event):
    if event_data.message_type != "group":
        BotController.send_message(QQRichText.QQRichText(QQRichText.Reply(event_data["message_id"]),f'管理功能\n*禁言/*ban （空格）（用户id，填all即全员禁言）（空格）（禁言时长，全员禁言无法设置时长）-禁言\n*解除禁言/*outban （空格）（用户id，填all即解除全员禁言）-解除禁言'),group_id=event_data.group_id)
        time.sleep(1)
    else:
        pass

EventManager.register_keyword("*ban ", ban)
EventManager.register_keyword("*禁言 ", ban)
EventManager.register_keyword("*outban ", out_ban)
EventManager.register_keyword("*解除禁言", out_ban)
EventManager.register_keyword("*禁言", helps,model="EQUAL")
EventManager.register_keyword("*ban", helps,model="EQUAL")

