import Lib.ExsManager,Lib.MuRainLib
from Lib import *
import os,time
import platform,psutil

api = OnebotAPI.OnebotAPI()
admin = Configs.GlobalConfig().bot_admin#管理员账号
welcomepic="https://static.codemao.cn/pickduck/HJoyN3rzkl.jpg"

class PluginInfo(ExsManager.PluginInfo):
    def __init__(self):
        super().__init__()
        self.NAME = "CTRL"  # 插件名称
        self.AUTHOR = "vika"  # 插件作者
        self.VERSION = "1.0.0"  # 插件版本
        self.DESCRIPTION = "控制功能"  # 插件描述
        self.IS_HIDDEN = True
        self.UID = "09c5-6a4e-f24cb01a-a0e945da-f026-30e7"



def reboot_pro(event_class, event_data: BotController.Event):
    if event_data.message_type == "group":# 判断是群聊事件还是私聊事件
        if str(event_data.user_id) in admin:
            BotController.send_message(QQRichText.QQRichText(QQRichText.At(event_data.user_id), " RESTARTING..."),group_id=event_data.group_id)
            restarttime=time.strftime("%H:%M:%S %Y-%m-%d", time.localtime())
            BotController.send_message(f'[Aoki]Bot restarted at {restarttime}', user_id=int(admin[0]))
            os.system("CLS")
            Lib.MuRainLib.restart()
    else:
        if str(event_data.user_id) in admin:
            restarttime=time.strftime("%H:%M:%S %Y-%m-%d", time.localtime())
            BotController.send_message(f'[Aoki]Bot restarted at {restarttime}', user_id=int(admin[0]))
            os.system("CLS")
            Lib.MuRainLib.restart()

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
    ae=BotController.api.get_version_info()
    basein=f'运行平台：{os_name}\n版本{os_version}（Python版本{python_version}）\nOneBot协议版本：{ae["protocol_version"]}\nOneBot实现：{ae["app_name"]}（版本{ae["app_version"]}）\n'
    hardr=f'CPU使用率：{cpu_per}%\n运行内存：已用{ram_use}MB，可用{ram_fre}MB，总计{ram_tot}MB\n硬盘：(C:\):{dis_free}GB/{dis_total}GB'
    final=f"状态\nAoki\n版本{main.VERSION}（{main.VERSION_WEEK}）\n库版本：{Lib.VERSION}（{Lib.VERSION_WEEK}）\n{basein}{hardr}"
    if event_data.message_type == "private":  # 判断是群聊事件还是私聊事件
        BotController.send_message(QQRichText.QQRichText(final), user_id=event_data.user_id)
    else:
        BotController.send_message(QQRichText.QQRichText(final),group_id=event_data.group_id)

def new_here(groupid):
    subfolder_count = 0
    path = os.path.join(data_path, "groups")
    # 遍历指定路径下的所有条目
    for entry in os.scandir(path):
        # 检查是否为文件夹
        if entry.is_dir():
            subfolder_count += 1
    
    BotController.send_message(f"Hello,I'm Aoki,have a great day\n———————————————\nGithub: https://github.com/GuzhMtangeroou/Aoki/ \n\nBased on:\nOnebot v11\nMuRainBot2\n已入驻{subfolder_count}个群组\n用户协议：https://static.codemao.cn/pickduck/SJ1KM8QOyx.pdf \n\n发送*help，开始使用", group_id=groupid)

def send_welcome_message(groupid):
    BotController.send_message(QQRichText.QQRichText("欢迎新人！",{"type": "image","data":{"file": f"{welcomepic}"}},f"\nAoki已入驻本群哦，发送*help开始使用吧~"),group_id=groupid)

def bot_has_kicked(out_time,groupid):
    BotController.send_message(QQRichText.QQRichText(f"[{out_time}]Bot被移出群聊{groupid}，若该操作非主动操作，请联系该群管理员"),user_id=admin[0])

def pong(event_class, event_data: BotController.Event):
    if event_data.meta_event_type == "private":
        BotController.send_message(QQRichText.QQRichText("pong!"), user_id=event_data.user_id)


EventManager.register_keyword("状态", get_info,model="EQUAL")
EventManager.register_keyword("RESTART", reboot_pro,model="EQUAL",cmdstart=False)
EventManager.register_keyword("ping", pong,model="EQUAL",cmdstart=False)