# coding:utf-8
import time
import threading
import os,sys
from Lib import*

def start_window():
    try:
        import tkinter as tk  
        startwindow=tk.Tk()
        startwindow.title('')
        startwindow.resizable(False,False)
        startwindow.overrideredirect(1)
        startwindow.wm_attributes("-topmost", True)
        w1=startwindow.winfo_screenwidth() #获取屏幕宽
        h1=startwindow.winfo_screenheight() #获取屏幕高
        w2=1024 #指定当前窗体宽
        h2=614 #指定当前窗体高
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
        pass

# 主函数
if __name__ == '__main__':
    if Configs.GlobalConfig().start_showpic == True:
        time.sleep(1)
        start_window()

    os.system("start cmd /k main.py")
    sys.exit(0)