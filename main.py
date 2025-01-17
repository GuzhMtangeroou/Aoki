# coding:utf-8
import threading
import Lib.MuRainLib
import Lib.ThreadPool
import Lib.GUILib
import os,platform,pystray
from PIL import Image
from pystray import MenuItem
import win32gui,win32con,win32api
from windows_toasts import Toast, WindowsToaster
from datetime import datetime

def machine_check():
    os_name = platform.system()
    os_version = platform.version()
    python_version=platform.python_version()
    if os_name == "Windows":
        if int(os_version.replace(".","")) >= int("6.3.9200".replace(".","")):
            if int(python_version.replace(".","")) >= int("3.11.4".replace(".","")):
                return 1
            else:
                return -3
        else:
            return -2
    else:
        return -1
checkcode=machine_check()
if checkcode == -1:
    print("版本错误，请下载正确的版本")
    Lib.MuRainLib.finalize_and_cleanup()
elif checkcode == -2:
    print(f"当前Windows版本过低，运行可能出现错误\n注意：我们将不会受理在此状态下运行的报错")
elif checkcode == -3:
    print(f"当前Python版本过低，运行可能出现错误\n注意：我们将不会受理在此状态下运行的报错")


BANNER = r"""
                _    _ 
     /\        | |  (_)
    /  \   ___ | | ___ 
   / /\ \ / _ \| |/ / |
  / ____ \ (_) |   <| |
 /_/    \_\___/|_|\_\_|                         
"""
BANNER_LINK = "https://github.com/GuzhMtangeroou/Aoki/"
VERSION = "1.0"  # 版本
VERSION_WEEK = "2025#1"  # 版本周
CHECK_CODE = 2501
console_window = win32gui.GetForegroundWindow()

def machine_check():
    os_name = platform.system()
    os_version = platform.version()
    python_version=platform.python_version()
    if os_name == "Windows":
        if os_version.replace(".","") >= "6.3.9200".replace(".",""):
            if python_version.replace(".","") >= "3.11.4".replace(".",""):
                return 1
            else:
                return -3
        else:
            return -2
    else:
        return -1

def color_text(text: str, text_color: tuple[int, int, int] = None, bg_color: tuple[int, int, int] = None):
    text = text + "\033[0m" if text_color is not None or bg_color is not None else text
    if text_color is not None:
        text = f"\033[38;2;{text_color[0]};{text_color[1]};{text_color[2]}m" + text
    if bg_color is not None:
        text = f"\033[48;2;{bg_color[0]};{bg_color[1]};{bg_color[2]}m" + text
    return text


def get_gradient(start_color: tuple[int, int, int], end_color: tuple[int, int, int], length: float):
    # length 为0-1的值，返回一个渐变色当前length的RGB颜色
    return (
        int(start_color[0] + (end_color[0] - start_color[0]) * length),
        int(start_color[1] + (end_color[1] - start_color[1]) * length),
        int(start_color[2] + (end_color[2] - start_color[2]) * length)
    )

def start_window():
    if Configs.GlobalConfig().start_showpic == True:        
        try:
            win32gui.ShowWindow(console_window, win32con.SW_MINIMIZE)
            time.sleep(1)
            import tkinter as tk  
            startwindow=tk.Tk()
            startwindow.title('')
            startwindow.resizable(False,False)
            startwindow.overrideredirect(1)
            startwindow.wm_attributes("-topmost", True)
            w1=startwindow.winfo_screenwidth() #获取屏幕宽
            h1=startwindow.winfo_screenheight() #获取屏幕高
            w2=Configs.GlobalConfig().startpic_w #指定当前窗体宽
            h2=Configs.GlobalConfig().startpic_h#指定当前窗体高
            startwindow.geometry("%dx%d+%d+%d"%(w2,h2,(w1-w2)/2,(h1-h2)/2))

            photo = tk.PhotoImage(file="Lib\\img\\start\\1.gif")
            # 显示图像
            label = tk.Label(startwindow, image=photo)
            label.pack()

            def autoClose():
                time.sleep(5)
                startwindow.destroy()
                

            t=threading.Thread(target=autoClose)
            t.start()

            startwindow.mainloop()
        except:
            return -1
        win32gui.ShowWindow(console_window, win32con.SW_NORMAL)
        return 1
    else:
        return 0

# 主函数
if __name__ == '__main__':
    import Lib.Configs as Configs
    if Configs.GlobalConfig().start_showcolorword:
        banner_start_color = (14, 190, 255)
        banner_end_color = (255, 66, 179)
        color_banner = ""
        banner = BANNER.split("\n")
        for i in range(len(banner)):
            for j in range(len(banner[i])):
                color_banner += color_text(
                    banner[i][j],
                    get_gradient(
                        banner_start_color,
                        banner_end_color,
                        ((j / (len(banner[i]) - 1) + i / (len(banner) - 1)) / 2)
                    )
                )
            color_banner += "\n"
        print(color_banner + color_text(BANNER_LINK, get_gradient(banner_start_color, banner_end_color, 0.5))
            + color_text("\n正在加载 Lib...", banner_start_color), end="")
    else:
        print(BANNER)
        print(BANNER_LINK)
        print("正在加载 Lib...")

    from Lib import *
    print(f"Lib 加载完成")
    api = OnebotAPI.OnebotAPI()
    Lib.ThreadPool.init()
    request_list = []
    logger = Logger.logger
    if start_window() == -1:
        logger.error("启动界面出现异常")

    logger.info(f"开始运行，当前版本：{VERSION}({VERSION_WEEK})")

    api = OnebotAPI.OnebotAPI()
    ThreadPool.init()
    request_list = []

    work_path = os.path.abspath(os.path.dirname(__file__))
    data_path = os.path.join(work_path, 'data')

    if not os.path.exists(data_path):
        os.makedirs(data_path)

    if not os.path.exists(cache_path):
        os.makedirs(cache_path)

    # TODO: 把废物的版本检测删了
    LibInfo.main_version, LibInfo.main_version_week = VERSION, VERSION_WEEK

    # 版本检测
    if LibInfo().version != LibInfo.main_version:
        logger.warning("库版本不是最新，可能会发生异常\n"
                       f"库版本:{LibInfo().version} Bot版本:{LibInfo.main_version}\n"
                       "注意：我们将不会受理在此状态下运行的报错")

    bot_uid = Configs.global_config.user_id
    bot_name = Configs.global_config.nick_name
    bot_admin = Configs.global_config.bot_admin

    PluginManager.load_plugins()
    if len(PluginManager.plugins) > 0:
        logger.info(f"插件导入完成，共成功导入 {len(PluginManager.plugins)} 个插件:")
        for plugin in PluginManager.plugins:
            try:
                plugin_info = plugin["plugin"].PluginInfo()
                if plugin_info.UID == "":
                    logger.warning("插件{} UID获取失败".format(plugin["name"]))
                else:
                    sed=Lib.PluginManager.on_extract(plugin_info.UID)
                    if sed >= CHECK_CODE:
                        logger.info(" - {}: {}  by {},UID:{}".format(plugin["name"], plugin_info.NAME, plugin_info.AUTHOR,plugin_info.UID))
                    elif sed < CHECK_CODE:
                        logger.info("插件{} 适配于较旧的Bot版本，请及时维护".format(plugin["name"]))
                    else:
                        logger.info("插件{} 校验失败".format(plugin["name"]))
            except ArithmeticError:
                logger.warning("插件{} 没有信息".format(plugin["name"]))
            except Exception as e:
                logger.warning("插件{} 信息获取失败: {}".format(plugin["name"], repr(e)))
    else:
        logger.warning("无插件成功导入！")

    logger.info("将以{}:{}启动监听服务器"
                .format(Configs.global_config.server_host, Configs.global_config.server_port))

    logger.info("将以{}调用API"
                .format(str(api)))

    # 检测bot名称与botUID是否为空或未设置
    if bot_uid is None or bot_name == "" or bot_uid == 123456 or bot_name is None:
        logger.info("BotUID或昵称来源：自动获取......")

        bot_info = api.get_login_info()
        if not isinstance(bot_info, dict):
            logger.error(f"获取BotUID与昵称失败，可能会导致严重问题({repr(bot_info)})")
            try:
                toaster = WindowsToaster('Python')
                newToast = Toast()
                newToast.text_fields = [f"获取BotUID与昵称失败，可能会导致严重问题：{repr(bot_info)}"]
                newToast.on_activated = lambda _: win32api.MessageBox(0, f"获取BotUID与昵称失败，可能会导致严重问题：{repr(bot_info)}", "Aoki", win32con.MB_ICONERROR)
                toaster.show_toast(newToast)    
            except:
                pass
        elif "user_id" in bot_info and "nickname" in bot_info:
            bot_uid, bot_name = bot_info["user_id"], bot_info["nickname"]
            raw_config = Configs.global_config.raw_config
            raw_config["account"]["user_id"] = bot_uid
            raw_config["account"]["nick_name"] = bot_name
            Configs.global_config.write_cache(raw_config)
            logger.debug("BotUID与昵称来源：自动获取")
        else:
            logger.error(f"获取BotUID与昵称失败，可能会导致严重问题{bot_info}")
            try:
                toaster = WindowsToaster('Python')
                newToast = Toast()
                newToast.text_fields = [f"获取BotUID与昵称失败，可能会导致严重问题：{repr(bot_info)}"]
                newToast.on_activated = lambda _: win32api.MessageBox(0, f"获取BotUID与昵称失败，可能会导致严重问题：{repr(bot_info)}", "Aoki", win32con.MB_ICONERROR)
                toaster.show_toast(newToast) 
            except:
                pass

    logger.info(f"欢迎使用 {Configs.global_config.nick_name}({Configs.global_config.user_id})")

    Command.start_command_listener()
    logger.info("开启命令输入")
    logininfo=BotController.api.get_login_info()

    # 禁用werkzeug的日志记录
    log = logging.getLogger('werkzeug')
    log.disabled = True
    
    """
    # 生命周期模拟
    if Configs.GlobalConfig().life_start:
        logger.info("生命周期侦测开始")
        def simulate_online():
            is_off=0
            while True:
                current_time = datetime.now()
                # 判断是否在22:00到9:00之间
                if Configs.GlobalConfig().life_start_offline_time <= current_time.hour < 24 or 0 <= current_time.hour < Configs.GlobalConfig().life_start_online_time:
                    if is_off==0:
                        logger.info(f"[生命周期]离线")
                        os.system(f"Lib\pkg\pssuspend.exe Lagrange.OneBot.exe")
                        is_off=1
                    else:
                        pass
                else:
                    is_off=0
                    offline_start_time = current_time
                    logger.info(f"[生命周期]离线状态开始")
                    offline_duration = random.randint(337, Configs.GlobalConfig().life_max_offline_time)
                    time.sleep(offline_duration)
                    offline_end_time = datetime.now()
                    logger.info(f"[生命周期]离线状态结束 ({offline_duration} 秒)")
                    online_start_time = current_time
                    logger.info(f"[生命周期]在线状态开始")
                    os.system(f"Lib\pkg\pssuspend.exe -r Lagrange.OneBot.exe")
                    online_duration = random.randint(1832, Configs.GlobalConfig().life_max_online_time)
                    time.sleep(online_duration)
                    online_end_time = datetime.now()
                    logger.info(f"[生命周期]在线状态结束 ({online_duration} 秒)")
        h=threading.Thread(target=simulate_online)
        h.start()
        """

    # 启动监听服务器
    try:
        logger.info("启动监听服务器")
        ListeningServer.server.serve_forever()
    except Exception as e:
        logger.error(f"监听服务器启动失败：{repr(e)}")
        toaster = WindowsToaster('Python')
        newToast = Toast()
        newToast.text_fields = [f"监听服务器启动失败：{repr(bot_info)}"]
        newToast.on_activated = lambda _: win32api.MessageBox(0, f"监听服务器启动失败：{repr(bot_info)}", "Aoki", win32con.MB_ICONERROR)
        toaster.show_toast(newToast) 
    finally:
        logger.info("监听服务器结束运行")

def exita():
    import gc
    gc.collect()
    Lib.MuRainLib.clean_cache()
    os.system("taskkill /f /im python.exe /t")

def baricon():
    # 托盘菜单
    menu: tuple = (
        MenuItem('重启', lambda: Lib.MuRainLib.restart()),
        MenuItem('退出', lambda: exita())       
        )

    image: Image = Image.open("Lib\\img\\ico\\1.ico")

    icon: pystray.Icon = pystray.Icon("name", title=f"Aoki-运行中\n版本{VERSION}（{VERSION_WEEK}）\n库版本：{Lib.VERSION}（{Lib.VERSION_WEEK}）", icon=image, menu=menu) # type: ignore
    icon.run()

l=threading.Thread(target=baricon)
l.start()