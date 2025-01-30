from Lib import *
import re

api = OnebotAPI.OnebotAPI()

#插件信息
class PluginInfo(ExsManager.PluginInfo):
    def __init__(self):
        super().__init__()
        self.NAME = "Play"  # 插件名称
        self.AUTHOR = "vika"  # 插件作者
        self.VERSION = "1.0.0"  # 插件版本
        self.DESCRIPTION = "三大平台音乐搜索+播放整合"  # 插件描述
        self.HELP_MSG = "发送“*Play”获取详细功能"  # 插件帮助
        self.IS_HIDDEN = False
        self.UID = "09c5-2cbb-36ac4b54-9ff182ab-3277-8ebe"

def Gethelp(event_class, event_data: BotController.Event):
    if event_data.message_type == "group":
        BotController.send_message(QQRichText.QQRichText(QQRichText.Reply(event_data["message_id"]),f'Play\n*163Play,id=（音乐id）-通过id获取音乐\n*163Play (歌曲名) (返回结果数量，默认10) (第几项，可直接播放)-网易云搜索+播放整合\n*QQPlay (歌曲名) (返回结果数量，默认10) (第几项，可直接播放)-QQ音乐搜索+播放整合\n*KugouPlay (歌曲名) (返回结果数量，默认10) (第几项，可直接播放)-酷狗搜索+播放整合\n*注：搜索功能中，歌名内空格用+代替；后两项参数可不带，别忘了空格！！；由于不可抗力，QQ音乐与酷狗获取的音乐无法直接发送语音，将发送直链！'),group_id=event_data.group_id)
        time.sleep(3)
    else:
        pass

def NeteaseMusicPlay_id(event_class, event_data: BotController.Event):
    if event_data.message_type == "group":  # 判断是群聊事件还是私聊事件
        rec=str(event_data.message)
        playid=get_id(rec)
        BotController.send_message(QQRichText.QQRichText(QQRichText.Reply(event_data["message_id"]), " 正在获取，请稍侯（若未发送歌曲则可能该歌曲为VIP歌曲或歌曲不存在）..."),group_id=event_data.group_id)
        BotController.send_message(QQRichText.QQRichText(
            {"type": "record",
            "data":{
                 "file": f"http://music.163.com/song/media/outer/url?id={playid}.mp3"
                 }
                 }
                 ),group_id=event_data.group_id)
    else:
        pass

def NeteaseMusicPlay_Link(event_class, event_data: BotController.Event):
    if event_data.message_type == "group":  # 判断是群聊事件还是私聊事件
        rec=str(event_data.message)
        playid=get_id(rec)
        BotController.send_message(QQRichText.QQRichText(QQRichText.Reply(event_data["message_id"]), " 正在获取，请稍侯（若未发送歌曲则可能该歌曲为VIP歌曲或歌曲不存在）..."),group_id=event_data.group_id)
        BotController.send_message(QQRichText.QQRichText(
            {"type": "record",
            "data":{
                 "file": f"http://music.163.com/song/media/outer/url?id={playid}.mp3"
                 }
                 }
                 ),group_id=event_data.group_id)
    else:
        pass


def NeteaseMusicSearch(event_class, event_data: BotController.Event):
    if event_data.message_type == "group":  # 判断是群聊事件还是私聊事件
        rec=str(event_data.message)
        recz=rec.split(" ")
        if len(recz) == 4:
            BotController.send_message(QQRichText.QQRichText(QQRichText.Reply(event_data["message_id"]), " 正在获取，请稍侯......"),group_id=event_data.group_id)
            searchkey=str(recz[-3])
            returnline=str(recz[-2])
            playline=str(recz[-1])
            ret=(requests.get(f"https://www.hhlqilongzhu.cn/api/dg_wyymusic.php?gm={searchkey}&num={returnline}&n={playline}").text).split("\n")[-1]
            playlink=get_playlink(ret)
            BotController.send_message(QQRichText.QQRichText(
            {"type": "record",
            "data":{
                "file": f"{playlink}"
                }
                }
                ),group_id=event_data.group_id)
        elif len(recz) == 3:
            searchkey=str(recz[-2])
            returnline=str(recz[-1])
            ret=(requests.get(f"https://www.hhlqilongzhu.cn/api/dg_wyymusic.php?gm={searchkey}&num={returnline}").text)
            BotController.send_message(QQRichText.QQRichText(QQRichText.Reply(event_data["message_id"]), f"搜索到以下歌曲\n{ret}"),group_id=event_data.group_id)
        elif len(recz) == 2:
            searchkey=str(recz[-1])
            ret=(requests.get(f"https://www.hhlqilongzhu.cn/api/dg_wyymusic.php?gm={searchkey}&num=10").text)
            BotController.send_message(QQRichText.QQRichText(QQRichText.Reply(event_data["message_id"]), f"搜索到以下歌曲\n{ret}"),group_id=event_data.group_id)
        else:
            BotController.send_message(QQRichText.QQRichText(QQRichText.Reply(event_data["message_id"]), "未知的指令或参数，请检查输入是否合法"),group_id=event_data.group_id)
    time.sleep(5)

def QQMusicSearch(event_class, event_data: BotController.Event):
    if event_data.message_type == "group":  # 判断是群聊事件还是私聊事件
        rec=str(event_data.message)
        recz=rec.split(" ")
        if len(recz) == 4:
            BotController.send_message(QQRichText.QQRichText(QQRichText.Reply(event_data["message_id"]), " 正在获取，请稍侯......"),group_id=event_data.group_id)
            searchkey=str(recz[-3])
            returnline=str(recz[-2])
            playline=str(recz[-1])
            ret=(requests.get(f"https://www.hhlqilongzhu.cn/api/dg_qqmusic.php?gm={searchkey}&num={returnline}&n={playline}").text).split("\n")[-1]
            BotController.send_message(QQRichText.QQRichText(f"{ret}"),group_id=event_data.group_id)
            # BotController.send_message(QQRichText.QQRichText(f"[CQ:record,file={cache_path}\{download_music_qq(get_playlink(ret))}]"),group_id=event_data.group_id)
        elif len(recz) == 3:
            searchkey=str(recz[-2])
            returnline=str(recz[-1])
            ret=(requests.get(f"https://www.hhlqilongzhu.cn/api/dg_qqmusic.php?gm={searchkey}&num={returnline}").text)
            BotController.send_message(QQRichText.QQRichText(QQRichText.Reply(event_data["message_id"]), f"搜索到以下歌曲\n{ret}"),group_id=event_data.group_id)
        elif len(recz) == 2:
            searchkey=str(recz[-1])
            ret=(requests.get(f"https://www.hhlqilongzhu.cn/api/dg_qqmusic.php?gm={searchkey}&num=10").text)
            BotController.send_message(QQRichText.QQRichText(QQRichText.Reply(event_data["message_id"]), f"搜索到以下歌曲\n{ret}"),group_id=event_data.group_id)
        else:
            BotController.send_message(QQRichText.QQRichText(QQRichText.Reply(event_data["message_id"]), "未知的指令或参数，请检查输入是否合法"),group_id=event_data.group_id)
    time.sleep(5)

def KugouMusicSearch(event_class, event_data: BotController.Event):
    if event_data.message_type == "group":  # 判断是群聊事件还是私聊事件
        rec=str(event_data.message)
        recz=rec.split(" ")
        if len(recz) == 4:
            BotController.send_message(QQRichText.QQRichText(QQRichText.Reply(event_data["message_id"]), " 正在获取，请稍侯......"),group_id=event_data.group_id)
            searchkey=str(recz[-3])
            returnline=str(recz[-2])
            playline=str(recz[-1])
            ret=(requests.get(f"https://www.hhlqilongzhu.cn/api/dg_kgmusic.php?gm={searchkey}&num={returnline}&n={playline}&type=json").text).split("\n")[-1]
            BotController.send_message(QQRichText.QQRichText(f"{ret}"),group_id=event_data.group_id)
        elif len(recz) == 3:
            searchkey=str(recz[-2])
            returnline=str(recz[-1])
            ret=(requests.get(f"https://www.hhlqilongzhu.cn/api/dg_kgmusic.php?gm={searchkey}&num={returnline}").text)
            BotController.send_message(QQRichText.QQRichText(QQRichText.Reply(event_data["message_id"]), f"搜索到以下歌曲\n{ret}"),group_id=event_data.group_id)
        elif len(recz) == 2:
            searchkey=str(recz[-1])
            ret=(requests.get(f"https://www.hhlqilongzhu.cn/api/dg_kgmusic.php?gm={searchkey}&num=10").text)
            BotController.send_message(QQRichText.QQRichText(QQRichText.Reply(event_data["message_id"]), f"搜索到以下歌曲\n{ret}"),group_id=event_data.group_id)
        else:
            BotController.send_message(QQRichText.QQRichText(QQRichText.Reply(event_data["message_id"]), "未知的指令或参数，请检查输入是否合法"),group_id=event_data.group_id)
    time.sleep(5)

EventManager.register_keyword("163Play，id=", NeteaseMusicPlay_id,model="BEGIN")
EventManager.register_keyword("music.163.com/#/song", NeteaseMusicPlay_Link,cmdstart=False)
EventManager.register_keyword("music.163.com/song", NeteaseMusicPlay_Link,cmdstart=False)
EventManager.register_keyword("163Play ", NeteaseMusicSearch,model="BEGIN")
EventManager.register_keyword("QQPlay ", QQMusicSearch,model="BEGIN")
EventManager.register_keyword("KugouPlay ", QQMusicSearch,model="BEGIN")
EventManager.register_keyword("Play", Gethelp,model="EQUAL")

def get_id(text):
    # 匹配url的正则表达式
    pattern = r'id=(\d+)'
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    else:
        return None
    
def get_playlink(text):
    pattern = r'播放链接：[^\s].+'
    match = re.search(pattern, text)
    if match:
        return match.group().replace("播放链接：","")
    else:
        return None