from Lib import *
import re
import Lib.MuRainLib

api = OnebotAPI.OnebotAPI()

#插件信息
class PluginInfo(PluginManager.PluginInfo):
    def __init__(self):
        super().__init__()
        self.NAME = "Play"  # 插件名称
        self.AUTHOR = "vika"  # 插件作者
        self.VERSION = "1.0.0"  # 插件版本
        self.DESCRIPTION = "三大平台音乐搜索+播放整合"  # 插件描述
        self.HELP_MSG = "发送“*Play”获取详细功能"  # 插件帮助
        self.IS_HIDDEN = False
        self.UID = "0964-fcdb-4b423f4e-52836a51-ef7d-ba1d"

def Gethelp(event_class, event_data: BotController.Event):
    if event_data.message_type == "group":
        BotController.send_message(QQRichText.QQRichText(QQRichText.Reply(event_data["message_id"]),f'Play\n*163Play,id=（音乐id）-通过id获取音乐\n*163Play (歌曲名) (返回结果数量，默认10) (第几项，可直接播放)-网易云搜索+播放整合\n*QQPlay (歌曲名) (返回结果数量，默认10) (第几项，可直接播放)-QQ音乐搜索+播放整合\n*KugouPlay (歌曲名) (返回结果数量，默认10) (第几项，可直接播放)-酷狗搜索+播放整合\n*注：搜索功能中，歌名内空格用+代替；后两项参数可不带，别忘了空格！！；由于不可抗力，QQ音乐与酷狗获取的音乐无法直接发送语音，将发送直链！'),group_id=event_data.group_id)
        time.sleep(3)
    else:
        pass

def NeteaseMusicPlay_id(event_class, event_data: BotController.Event):
    if event_data.message_type == "group":  # 判断是群聊事件还是私聊事件
        rec=str(event_data.message)
        playid=str(rec.split(' ')[-1])
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

EventManager.register_keyword("*163Play，id=", NeteaseMusicPlay_id,model="BEGIN")
EventManager.register_keyword("https://music.163.com/#/song", NeteaseMusicPlay_Link,model="BEGIN")
EventManager.register_keyword("*163Play,id=", NeteaseMusicPlay_id,model="BEGIN")
EventManager.register_keyword("*163Play ", NeteaseMusicSearch,model="BEGIN")
EventManager.register_keyword("*QQPlay ", QQMusicSearch,model="BEGIN")
EventManager.register_keyword("*KugouPlay ", QQMusicSearch,model="BEGIN")
EventManager.register_keyword("*Play", Gethelp,model="EQUAL")

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
    
def get_permanent_link(url):
    # 使用requests库发送head请求
    response = requests.head(url, allow_redirects=True)
    # 检查是否有重定向发生
    if 'location' in response.headers:
        # 如果响应头中包含'location'，则表示发生了重定向
        # 递归调用自身以处理连续重定向的情况
        return get_permanent_link(response.headers['location'])
    else:
        # 如果没有重定向，则返回当前请求的URL作为永久链接
        return response.url

def download_music_qq(url):
    file_name = f'{str(url).split(".")[-1].split("&")[0]}'
    heads={"cookie":"ptcz=898c37f640cdd21ecfaed2185f75d96dd04236ca1936535d86dfb7eb17e116bc; pgv_pvid=5794844486; iip=0; _qimei_uuid42=1820315142e100686550d018077da0c6de3536c12b; _qimei_fingerprint=d3c60c3b650720acc14bcdd8e80ce840; _qimei_q36=; _qimei_h38=2db8a0446550d018077da0c60200000e418203; suid=0_ea85ea43465bb"}
    response = requests.get(url,headers=heads)
    path=f"./data/cache/{file_name}"
    with open(path, 'wb') as file:
        file.write(response.content)
    return file_name