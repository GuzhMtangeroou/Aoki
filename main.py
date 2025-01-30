# coding:utf-8
from Lib import*
import os,time,platform

def machine_check():
    os_name = platform.system()
    os_version = platform.version()
    python_version=platform.python_version()
    if os_name == "Linux":
            if int(python_version.replace(".","")) >= int("3.11.4".replace(".","")):
                return 1
            else:
                return -3
    else:
        return -1

checkcode=machine_check()
if checkcode == -1:
    print("版本错误，请下载正确的版本")
    time.sleep(3)
    finalize_and_cleanup()
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


# 主函数
if __name__ == '__main__':
    print(BANNER)
    print(BANNER_LINK)
    api = OnebotAPI.OnebotAPI()
    ThreadPool.init()
    logger = Logger.logger

    api = OnebotAPI.OnebotAPI()
    ThreadPool.init()

    work_path = os.path.abspath(os.path.dirname(__file__))
    data_path = os.path.join(work_path, 'data')

    if not os.path.exists(data_path):
        os.makedirs(data_path)

    if not os.path.exists(cache_path):
        os.makedirs(cache_path)

    bot_uid = Configs.global_config.user_id
    bot_name = Configs.global_config.nick_name
    bot_admin = Configs.global_config.bot_admin

    ExsManager.load_plugins()
    if len(ExsManager.plugins) > 0:
        logger.info(f"共导入 {len(ExsManager.plugins)} 个插件，成功项如下：")
        for plugin in ExsManager.plugins:
            try:
                plugin_info = plugin["prog"].PluginInfo()
                if plugin_info.UID == "":
                    logger.warning("插件{} UID获取失败".format(plugin["name"]))
                else:
                    sed=ExsManager.on_extract(plugin_info.UID)
                    if sed >= UPDATE_CHECK_CODE:
                        logger.info(" - {}: {}  by {},UID:{}".format(plugin["name"], plugin_info.NAME, plugin_info.AUTHOR,plugin_info.UID))
                    elif sed < UPDATE_CHECK_CODE:
                        logger.info("插件{} 适配于较旧的Bot版本，请及时维护".format(plugin["name"]))
                    else:
                        logger.info("插件{} 校验失败".format(plugin["name"]))
            except ArithmeticError:
                logger.warning("插件{} 没有信息".format(plugin["name"]))
            except Exception as e:
                logger.warning("插件{} 信息获取失败: {}".format(plugin["name"], repr(e)))
    else:
        logger.warning("无插件成功导入")

    logger.info("将以{}:{}启动监听服务器"
                .format(Configs.global_config.server_host, Configs.global_config.server_port))

    logger.info("将以{}调用API"
                .format(str(api)))

    # 检测bot名称与botUID是否为空或未设置
    if bot_uid is None or bot_name == "" or bot_uid == 123456 or bot_name is None:
        logger.info("BotUID或昵称来源：自动获取")

        bot_info = api.get_login_info()
        if not isinstance(bot_info, dict):
            logger.error(f"获取BotUID与昵称失败，可能会导致严重问题({repr(bot_info)})")
        elif "user_id" in bot_info and "nickname" in bot_info:
            bot_uid, bot_name = bot_info["user_id"], bot_info["nickname"]
            raw_config = Configs.global_config.raw_config
            raw_config["account"]["user_id"] = bot_uid
            raw_config["account"]["nick_name"] = bot_name
            Configs.global_config.write_cache(raw_config)
            logger.debug("BotUID与昵称来源：自动获取")
        else:
            logger.error(f"获取BotUID与昵称失败，可能会导致严重问题{bot_info}")

    logger.info(f"欢迎使用 {Configs.global_config.nick_name}({Configs.global_config.user_id})")

    Command.start_command_listener()
    logger.info("开启命令输入")
    logininfo=BotController.api.get_login_info()

    # 禁用werkzeug的日志记录
    log = logging.getLogger('werkzeug')
    log.disabled = True
    # 启动监听服务器
    try:
        logger.info("启动监听服务器")
        ListeningServer.server.serve_forever()
    except Exception as e:
        logger.error(f"监听服务器启动失败：{repr(e)}")
    finally:
        logger.info("监听服务器结束运行")