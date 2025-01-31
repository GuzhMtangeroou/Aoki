import os
import importlib
import time
import Lib.Logger as Logger
import Lib.ThreadPool as ThreadPool
import struct

logger = Logger.logger

plugins: list[dict] = []
work_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
extensions_path = os.path.join(work_path, "extensions")

if not os.path.exists(extensions_path):
    os.makedirs(extensions_path)


def load_plugins():
    global plugins
    # 获取插件目录下的所有文件
    things_in_plugin_dir = os.listdir(extensions_path)

    # 筛选出后缀为.py的文件
    def mapper(name, plugin_suffix=None):
        if plugin_suffix is None:
            plugin_suffix = [".py", ".pyc"]
        for i in plugin_suffix:
            if name.endswith(i):
                return name.split(".")[0]
            else:
                return ""

    things_in_plugin_dir = map(mapper, things_in_plugin_dir)
    things_in_plugin_dir = [_ for _ in things_in_plugin_dir if _ != ""]

    plugins = []

    for i in things_in_plugin_dir:
        try:
            # 导入插件
            t = time.time()
            logger.debug(f"正在加载插件: {i}:")
            plugin_info={"name": i, "prog": importlib.import_module('.' + i, package='extensions')}
            plugins.append(plugin_info)
            logger.debug(f"插件 {i} 加载成功,，耗时 {round(time.time() - t, 2)}s")
        except Exception as e:
            logger.error(f"加载插件 {i} 失败，原因:{repr(e)}")

    plugins.sort(key=lambda x: x["name"])

    return plugins


class PluginInfo:
    def __init__(self):
        self.NAME:str = ""  # 插件名称
        self.AUTHOR:str = ""  # 插件作者
        self.VERSION:str = ""  # 插件版本
        self.DESCRIPTION:str = ""  # 插件描述
        self.HELP_MSG:str = ""  # 插件帮助
        self.IS_HIDDEN:bool = False  # 插件是否隐藏（在/help命令中）
        self.UID:str = "" #插件UID

def extract_seed(identifier):
    # Remove dashes from the identifier
    clean_hex = identifier.replace('-', '')
    # Extract the first 4 characters which represent the seed in hexadecimal
    seed_hex = clean_hex[:4]
    # Convert the hexadecimal back to an integer
    seed_int = struct.unpack('>H', bytes.fromhex(seed_hex))[0]
    return seed_int


def on_extract(entry:str):
    try:
        identifier = entry.strip()
        seed = extract_seed(identifier)
        return seed
    except:
        return -1

@ThreadPool.async_task
def run_plugin_main(data):
    global plugins
    for plugin in plugins:
        try:
            if not callable(plugin["prog"].main):
                continue
        except AttributeError:
            continue

        logger.debug(f"执行插件: {plugin['name']}")
        try:
            plugin["prog"].main(data.event_json, work_path)
        except Exception as e:
            logger.error(f"执行插件{plugin['name']}时发生错误: {repr(e)}")
            continue
