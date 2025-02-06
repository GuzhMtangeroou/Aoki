import os
import yaml
from Lib import FileCacher

work_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
data_path = os.path.join(work_path, "data")
exs_config_path = os.path.join(work_path, "extensions_configs")

def change_dic(a):
    if a == "auto":
        return 0
    else:
        global exs_config_path
        exs_config_path = a
        return 1

if not os.path.exists(exs_config_path):
    os.makedirs(exs_config_path)

DEFAULT_CONFIG="""
#配置文件

#账号
account: # 账号相关
  user_id:    # QQ账号（留空则自动获取）
  nick_name: "" #昵称（留空则自动获取）
  bot_admin: []

#网络
api: # Api设置
  host: '127.0.0.1'
  port: 5700

server: # 监听服务器设置
  host: '127.0.0.1'
  port: 5701
  
#命令
command:  # 命令相关
  command_start: "*"  # 命令起始符

extensions: # 插件相关自定义设置
  dictionary: 'auto' #插件目录（默认auto，即同文件夹下的“extensions”目录
  configdic: 'auto' #插件目录（默认auto，即同文件夹下的“extensions_configs”目录

auto_check_update: #自动更新（仅启动时检测）
  enable: false #是否启用
  auto_download: true #是否自动下载

#其他
thread_pool: 
  max_workers: 12 # 线程池最大线程数

qq_data_cache:  # QQ数据缓存设置
  enable: true  # 是否启用缓存（非常不推荐关闭缓存，对于对于需要无缓存的场景，推荐在插件内自行调用api来获取而非关闭此配置项）
  expire_time: 300  # 缓存过期时间（秒）
  max_cache_size: 500  # 最大缓存数量（设置过大可能会导致报错）


debug: # 调试模式
  enable: false # 是否启用调试模式

auto_restart_onebot:  # 在Onebot实现端状态异常时自动重启Onebot实现端（需开启心跳包）
  enable: true  # 是否启用自动重启
"""

class Config:
    def __init__(self, path):
        self.raw_config = None
        self.path = path
        self.encoding = "utf-8"
        self.default_config = DEFAULT_CONFIG

    def reload(self):
        if os.path.exists(self.path):
            try:
                self.raw_config = FileCacher.read_file(self.path, self.encoding)
                if isinstance(self.raw_config, str):
                    self.raw_config = yaml.load(self.raw_config, yaml.FullLoader)
            except Exception as e:
                print(f"配置文件加载失败，请检查配置文件内容是否正确。"
                             f"如果无法修复，请删除配置文件重新配置，以创建默认配置文件。"
                             f"错误信息：{repr(e)}")
        else:
            try:
                if isinstance(self.default_config, str):
                    with open(self.path, "w", encoding="utf-8") as f:
                        f.write(self.default_config)
                        print("配置文件不存在，已创建默认配置文件")
                    self.reload()
                elif isinstance(self.default_config, dict):
                    with open(self.path, "w", encoding="utf-8") as f:
                        yaml.safe_dump(self.default_config, f)
                        print("配置文件不存在，已创建默认配置文件")
                    self.reload()
                else:
                    print("配置文件不存在，且未提供默认配置，无法创建默认配置文件")
                    self.config = {}
            except Exception as e:
                print(f"配置文件创建失败，请检查配置文件路径是否正确。错误信息：{repr(e)}")
                self.config = {}
        return self

    def save_default(self, default_config: str):
        if isinstance(default_config, str):
            FileCacher.write_non_existent_file(self.path, default_config, self.encoding)
        else:
            raise TypeError("default config must be a string")
        return self

    def write_cache(self, item):
        FileCacher.write_cache(self.path, item)

    def get_config(self):
        return self.raw_config


class GlobalConfig(Config):
    def __init__(self):
        super().__init__("config.yml")
        self.reload()
        self.user_id = self.raw_config["account"]["user_id"]
        self.nick_name = self.raw_config["account"]["nick_name"]
        self.bot_admin = self.raw_config["account"]["bot_admin"]
        self.server_host = self.raw_config["server"]["host"]
        self.server_port = self.raw_config["server"]["port"]
        self.api_host = self.raw_config["api"]["host"]
        self.api_port = self.raw_config["api"]["port"]
        self.max_workers = self.raw_config["thread_pool"]["max_workers"]
        self.qq_data_cache = self.raw_config["qq_data_cache"]["enable"]
        self.expire_time = self.raw_config["qq_data_cache"]["expire_time"]
        self.max_cache_size = self.raw_config["qq_data_cache"]["max_cache_size"]
        self.debug = self.raw_config["debug"]["enable"]
        self.auto_restart_onebot = self.raw_config["auto_restart_onebot"]["enable"]
        self.command_start = self.raw_config["command"]["command_start"]
        self.auto_check_update = self.raw_config["auto_check_update"]["enable"]
        self.auto_download_update = self.raw_config["auto_check_update"]["auto_download"]
        self.exdic = self.raw_config["extensions"]["dictionary"]
        self.exconfdic = self.raw_config["extensions"]["configdic"]
    def write_cache(self, item):
        super().write_cache(item)
        self.__init__()

global_config = GlobalConfig()
