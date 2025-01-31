# coding:utf-8

import os
# 修改工作目录
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Lib.MuRainLib import *
from PIL import Image
import Lib.OnebotAPI as OnebotAPI
import Lib.QQRichText as QQRichText
import Lib.EventManager as EventManager
import Lib.Logger as Logger
import Lib.BotController as BotController
import Lib.Configs as Configs
import Lib.FileCacher as FileCacher
import Lib.ThreadPool as ThreadPool
import Lib.ListeningServer as ListeningServer
import Lib.ExsManager as ExsManager
import Lib.QQDataCacher as QQDataCacher
import Lib.Command as Command
import main as main
import platform

# 扩展模块
import Lib.AddtionPackage as AddtionPackage

VERSION = "1.0"
VERSION_WEEK = "25#2"
UPDATE_CHECK_CODE = int(VERSION_WEEK.replace("#","0"))


# Lib信息
class LibInfo:
    def __init__(self):
        self.version = VERSION
        self.version_week = VERSION_WEEK
        self.update_version_code = UPDATE_CHECK_CODE
        self.os = platform.system()