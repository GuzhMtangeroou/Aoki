"""
MuRainLib
用于MuRain Bot框架
"""
import atexit
import hashlib
import logging
import os
import sys
import requests,urllib3
import shutil
import time,json,zipfile
import random
from collections import OrderedDict
import Lib.Logger as Logger

#  ____                     _                 __  __       _____       _       ____        _   ___  
# |  _ \                   | |               |  \/  |     |  __ \     (_)     |  _ \      | | |__ \ 
# | |_) | __ _ ___  ___  __| |   ___  _ __   | \  / |_   _| |__) |__ _ _ _ __ | |_) | ___ | |_   ) |
# |  _ < / _` / __|/ _ \/ _` |  / _ \| '_ \  | |\/| | | | |  _  // _` | | '_ \|  _ < / _ \| __| / / 
# | |_) | (_| \__ \  __/ (_| | | (_) | | | | | |  | | |_| | | \ \ (_| | | | | | |_) | (_) | |_ / /_ 
# |____/ \__,_|___/\___|\__,_|  \___/|_| |_| |_|  |_|\__,_|_|  \_\__,_|_|_| |_|____/ \___/ \__|____|

work_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
data_path = os.path.join(work_path, "data")
logs_path = os.path.join(work_path, "logs")
cache_path = os.path.join(data_path, "cache")
logger = Logger.logger


class LimitedSizeDict(OrderedDict):
    def __init__(self, max_size):
        self._max_size = max_size
        super().__init__()

    def __setitem__(self, key, value):
        if key in self:
            del self[key]
        elif len(self) >= self._max_size:
            oldest_key = next(iter(self))
            del self[oldest_key]
        super().__setitem__(key, value)


def restart() -> None:
    # 获取当前解释器路径
    p = sys.executable
    try:
        # 启动新程序(解释器路径, 当前程序)
        os.execl(p, p, *sys.argv)
    except OSError:
        # 关闭当前程序
        sys.exit()

def Check_upd():
    urllib3.disable_warnings()
    headers={
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36"
    }
    a=requests.get("https://guzhmtangeroou.github.io/api.aoki.github.io/Version.json",headers=headers,verify=False)
    b=json.loads(a.text)
    return b

def Download_upd(url, local_filename): 
    # 发送HTTP请求获取远程文件
    with requests.get(url, stream=True,verify=False) as r:
        r.raise_for_status()  # 检查请求是否成功
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                if chunk:  # 过滤掉保持活动的没有数据的块
                    f.write(chunk)
                    f.flush()

    return local_filename

# 删除缓存文件
def clean_cache() -> None:
    if os.path.exists(cache_path):
        try:
            shutil.rmtree(cache_path, ignore_errors=True)
        except Exception as e:
            logging.warning("删除缓存时报错，报错信息: %s" % repr(e))


# 函数缓存
def function_cache(max_size: int, expiration_time: int = -1):
    cache = LimitedSizeDict(max_size)

    def cache_decorator(func):
        def wrapper(*args, **kwargs):
            key = str(func.__name__) + str(args) + str(kwargs)
            if key in cache and (expiration_time == -1 or time.time() - cache[key][1] < expiration_time):
                return cache[key][0]
            result = func(*args, **kwargs)
            cache[key] = (result, time.time())
            return result

        def clear_cache():
            """清理缓存"""
            cache.clear()

        def get_cache():
            """获取缓存"""
            return dict(cache)

        def original_func(*args, **kwargs):
            """调用原函数"""
            return func(*args, **kwargs)

        wrapper.clear_cache = clear_cache
        wrapper.get_cache = get_cache
        wrapper.original_func = original_func
        return wrapper

    return cache_decorator

# 结束运行
@atexit.register
def finalize_and_cleanup():
    logger.info("即将关闭，正在删除缓存")

    clean_cache()
    restarttime=time.strftime("%H:%M:%S %Y-%m-%d", time.localtime())
    logger.info(f'[Aoki]Bot exited at {restarttime}')
    quit()