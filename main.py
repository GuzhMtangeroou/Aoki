# coding:utf-8
import atexit
import threading
import Lib.ThreadPool
from Lib import *
import os
import win32gui

BANNER = r"""
                _    _ 
     /\        | |  (_)
    /  \   ___ | | ___ 
   / /\ \ / _ \| |/ / |
  / ____ \ (_) |   <| |
 /_/    \_\___/|_|\_\_|                         
https://github.com/GuzhMtangeroou/Aoki/
"""

logger = Logger.logger
VERSION = "1.0"  # 版本
VERSION_WEEK = "2024#4"  # 版本周

api = OnebotAPI.OnebotAPI()
Lib.ThreadPool.init()
request_list = []

work_path = os.path.abspath(os.path.dirname(__file__))
data_path = os.path.join(work_path, 'data')
yaml_path = os.path.join(work_path, 'config.yml')
cache_path = os.path.join(data_path, "cache")

if not os.path.exists(data_path):
    os.makedirs(data_path)

if not os.path.exists(cache_path):
    os.makedirs(cache_path)

# 主函数
if __name__ == '__main__':
    os.system("CLS")
    logger.info(f"当前版本：{VERSION}({VERSION_WEEK})")
    print(BANNER)

    LibInfo.main_version, LibInfo.main_version_week = VERSION, VERSION_WEEK

    bot_uid = Configs.GlobalConfig().user_id
    bot_name = Configs.GlobalConfig().nick_name
    bot_admin = Configs.GlobalConfig().bot_admin

    PluginManager.load_plugins()
    if len(PluginManager.plugins) > 0:
        logger.info("插件导入完成，共导入 {} 个插件:".format(len(PluginManager.plugins)))
        for plugin in PluginManager.plugins:
            try:
                plugin_info = plugin["plugin"].PluginInfo()
                logger.info(" - %s: %s 作者:%s" % (plugin["name"], plugin_info.NAME, plugin_info.AUTHOR))
            except ArithmeticError:
                logger.warning("插件{} 没有信息".format(plugin["name"]))
            except Exception as e:
                logger.warning("插件{} 信息获取失败: {}".format(plugin["name"], repr(e)))
    else:
        logger.warning("无插件成功导入！")

    logger.info("读取到监听服务器ip，将以此ip启动监听服务器: {}:{}"
                .format(Configs.GlobalConfig().server_host, Configs.GlobalConfig().server_port))

    logger.info("读取到监听api，将以此url调用API: {}"
                .format(str(api)))

    # 检测bot名称与botUID是否为空或未设置
    if bot_uid is None or bot_name == "" or bot_uid == 123456 or bot_name is None:
        logger.info("配置文件中未找到BotUID或昵称，正在自动获取")

        bot_info = api.get_login_info()
        if not isinstance(bot_info, dict):
            logger.error(f"获取BotUID与昵称失败，可能会导致严重问题({repr(bot_info)})")
        elif "user_id" in bot_info and "nickname" in bot_info:
            bot_uid, bot_name = bot_info["user_id"], bot_info["nickname"]
            raw_config = Configs.GlobalConfig().raw_config
            raw_config["account"]["user_id"] = bot_uid
            raw_config["account"]["nick_name"] = bot_name
            Configs.GlobalConfig().write_cache(raw_config)
            logger.debug("成功获取BotUID与昵称")
        else:
            logger.error(f"获取BotUID与昵称失败，字段缺失，可能会导致严重问题。{bot_info}")

    logger.info(f"登录用户： {Configs.GlobalConfig().nick_name}({Configs.GlobalConfig().user_id})")

    threading.Thread(target=Command.start_listening_command, daemon=True).start()
    logger.info("开启命令输入")

    # 禁用werkzeug的日志记录
    log = logging.getLogger('werkzeug')
    log.disabled = True

    # 启动监听服务器
    try:
        logger.info("启动监听服务器")
        ListeningServer.server.serve_forever()
    except Exception as e:
        logger.error("监听服务器启动失败，报错信息：{}".format(repr(e)))
    finally:
        logger.info("监听服务器结束运行")
