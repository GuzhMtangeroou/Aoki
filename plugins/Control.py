import Lib.PluginManager,Lib.MuRainLib
from Lib import *
import os,time
import platform,psutil

api = OnebotAPI.OnebotAPI()
admin = ["3569709728","403253","3876750974"]#管理员账号

class PluginInfo(PluginManager.PluginInfo):
    def __init__(self):
        super().__init__()
        self.NAME = "CTRL"  # 插件名称
        self.AUTHOR = "vika"  # 插件作者
        self.VERSION = "1.0.0"  # 插件版本
        self.DESCRIPTION = "控制功能"
        self.IS_HIDDEN = False
        self.UID = "0964-fcdb-4b423f4e-52836a51-ef7d-ba1d"  # 插件描述



def reboot_pro(event_class, event_data: BotController.Event):
    if event_data.message_type == "group":# 判断是群聊事件还是私聊事件
        if str(event_data.user_id) in admin:
            BotController.send_message(QQRichText.QQRichText(QQRichText.At(event_data.user_id), " RESTARTING..."),group_id=event_data.group_id)
            restarttime=time.strftime("%H:%M:%S %Y-%m-%d", time.localtime())
            BotController.send_message(f'[Kaya]Bot restarted at {restarttime}', user_id=int(admin[0]))
            os.system("CLS")
            os.system("main.py")
            Lib.MuRainLib.reboot()
    else:
        if str(event_data.user_id) in admin:
            restarttime=time.strftime("%H:%M:%S %Y-%m-%d", time.localtime())
            BotController.send_message(f'[Kaya]Bot restarted at {restarttime}', user_id=int(admin[0]))
            os.system("CLS")
            os.system("main.py")
            Lib.MuRainLib.reboot()

def get_info(event_class, event_data: BotController.Event):
    python_version = platform.python_version()
    os_name = platform.system()
    os_version = platform.version()
    cpu_per=psutil.cpu_percent(interval=1)
    python_version=platform.python_version()
    ram_usage = psutil.virtual_memory()
    ram_tot=round(ram_usage.total / 1024 / 1024)
    ram_fre=round(ram_usage.available / 1024 / 1024)
    ram_use=round(ram_usage.used / 1024 / 1024)
    dk = psutil.disk_usage('/')
    dis_total = round(dk.total / 1024 / 1024 / 1024)
    dis_free = round(dk.free / 1024 / 1024 / 1024)
    basein=f'运行平台：{os_name}\n版本{os_version}（Python版本{python_version}）\n'
    hardr=f'CPU使用率：{cpu_per}%\n运行内存：已用{ram_use}MB，可用{ram_fre}MB，总计{ram_tot}MB\n硬盘：(C:\):{dis_free}GB/{dis_total}GB'
    final=f"状态\nAoki\n版本：{Lib.VERSION}（{Lib.VERSION_WEEK}）\n \n{basein}{hardr}"
    if event_data.message_type == "private":  # 判断是群聊事件还是私聊事件
        BotController.send_message(final, user_id=event_data.user_id)
    else:
        BotController.send_message(QQRichText.QQRichText(final),group_id=event_data.group_id)

def new_here(groupid):
    BotController.send_message(f"「こにちわ。青木です」\n———————————————\nAoki - 一只小小的QQ Bot\nGithub: https://github.com/GuzhMtangeroou/Aoki/\n\nBased on:\nOnebot v11\nMuRainBot2\n\n发送*help，开始使用", group_id=groupid)

EventManager.register_keyword("/状态", get_info,model="EQUAL")
EventManager.register_keyword("RESTART", reboot_pro,model="EQUAL")

