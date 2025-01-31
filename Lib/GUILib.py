import Lib.BotController as BotController
import Lib.EventManager
import Lib.QQRichText as QQRichText
import Lib.MuRainLib as MuRainLib
import Lib.Logger as Logger
import Lib
import sys,win32api,win32con
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit,QProgressBar
from PyQt5.QtGui import QIntValidator,QPixmap
from PyQt5.QtCore import Qt

logger = Logger.logger

def SEND_MSG_TO_USER():
    def clicked(user_id_input, text_input):
        text = text_input.toPlainText()  # 获取多行文本框的内容
        user_id = int(user_id_input.text())
        BotController.send_message(QQRichText.QQRichText(text), user_id=user_id)
        app.quit()

    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle('发送消息到用户')
    window.setGeometry(100, 100, 400, 200)

    layout = QVBoxLayout()

    # 创建第一行布局
    first_row_layout = QHBoxLayout()
    lbl_userID = QLabel('发送到用户', window)
    user_id_input = QLineEdit(window)
    user_id_input.setValidator(QIntValidator())  # 设置验证器以仅允许整数输入
    first_row_layout.addWidget(lbl_userID)
    first_row_layout.addWidget(user_id_input)
    layout.addLayout(first_row_layout)

    # 创建第二行布局
    second_row_layout = QHBoxLayout()
    lbl_text = QLabel('发送内容', window)
    text_input = QTextEdit(window)  # 使用QTextEdit作为多行文本框
    second_row_layout.addWidget(lbl_text)
    second_row_layout.addWidget(text_input)
    layout.addLayout(second_row_layout)

    # 创建按钮
    btn_send = QPushButton('发送', window)
    btn_send.clicked.connect(lambda: clicked(user_id_input, text_input))
    layout.addWidget(btn_send)

    window.setLayout(layout)
    window.show()

    app.exec_()

def SEND_MSG_TO_GROUP():
    
    def clicked(user_id_input, text_input):
        text = text_input.toPlainText()  # 获取多行文本框的内容
        user_id = int(user_id_input.text())
        BotController.send_message(QQRichText.QQRichText(text), group_id=user_id)
        window.close()

    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle('发送消息到群')
    window.setGeometry(100, 100, 400, 200)

    layout = QVBoxLayout()

    # 创建第一行布局
    first_row_layout = QHBoxLayout()
    lbl_userID = QLabel('发送到群', window)
    user_id_input = QLineEdit(window)
    user_id_input.setValidator(QIntValidator())  # 设置验证器以仅允许整数输入
    first_row_layout.addWidget(lbl_userID)
    first_row_layout.addWidget(user_id_input)
    layout.addLayout(first_row_layout)

    # 创建第二行布局
    second_row_layout = QHBoxLayout()
    lbl_text = QLabel('发送内容', window)
    text_input = QTextEdit(window)  # 使用QTextEdit作为多行文本框
    second_row_layout.addWidget(lbl_text)
    second_row_layout.addWidget(text_input)
    layout.addLayout(second_row_layout)

    # 创建按钮
    btn_send = QPushButton('发送', window)
    btn_send.clicked.connect(lambda: clicked(user_id_input, text_input))
    layout.addWidget(btn_send)

    window.setLayout(layout)
    window.show()
    app.exec_()

def ABOUT():
    import main as main
    # 每个Qt应用必须有一个QApplication实例
    app = QApplication(sys.argv)

    # 创建窗口
    window = QWidget()
    window.setWindowTitle('About')

    # 加载图片
    image_label = QLabel()
    pixmap = QPixmap('Lib\\img\\about.png')  # 替换为你的图片路径
    image_label.setPixmap(pixmap)

    # 创建文本标签并设置文本内容
    text_label = QLabel(f'Aoki\n版本：{main.VERSION}（{main.VERSION_WEEK}）\n库版本：{Lib.VERSION}（{Lib.VERSION_WEEK}）')
    text_label.setAlignment(Qt.AlignCenter)  # 文本居中对齐

    # 创建布局管理器并将控件添加到布局中
    layout = QVBoxLayout()
    layout.addWidget(image_label)
    layout.addWidget(text_label)

    # 设置窗口的布局
    window.setLayout(layout)

    # 根据图片大小调整窗口大小
    window.resize(pixmap.width(), pixmap.height() + text_label.sizeHint().height())

    # 显示窗口
    window.show()
    # 进入Qt事件循环
    app.exec_()

def UPDATE():
    def initUI(window, text_box, progress_bar, button):
        window.setWindowTitle('检查更新')
        layout = QVBoxLayout()

        layout.addWidget(text_box)

        layout.addWidget(progress_bar)

        button.clicked.connect(lambda: check_update(text_box, progress_bar, window))
        layout.addWidget(button)

        window.setLayout(layout)
        window.resize(300, 200)
        window.show()

    def check_update(text_box, progress_bar, window):
        text_box.setText("正在检查更新...")
        try:
            dat = MuRainLib.Check_upd()
            if dat["code"] == 0:
                text_box.setText("获取更新信息完成")
                current_version = Lib.LibInfo().update_version_code
                latest_version = dat["data"]["LatestVersionWeek"]
                if latest_version != current_version:
                    download_update(dat["data"]["UpdLink-win32"], text_box, progress_bar, window)
                else:
                    window.close()
                    win32api.MessageBox(0, "已是最新版本", "Aoki", win32con.MB_OK)
            else:
                text_box.setText(f"检查更新失败: {dat.get('message', '未知错误')}")
        except Exception as e:
            text_box.setText(f"检查更新失败: {str(e)}")
            set_progress_bar_to_error(progress_bar)

    def download_update(url, text_box, progress_bar, window):
        local_filename = url.split('/')[-1]
        text_box.setText(f"正在下载新版本: {local_filename}")
        progress_bar.setMaximum(0)  # Indeterminate progress bar
        try:
            downloaded_file = MuRainLib.Download_upd(url, local_filename, progress_callback=lambda block_num, block_size, total_size: update_progress(block_num, block_size, total_size, progress_bar))
            window.close()
            win32api.MessageBox(0, f"下载更新“{downloaded_file}”完成，请手动安装", "Aoki", win32con.MB_OK)
        except Exception as e:
            text_box.setText(f"下载更新失败: {str(e)}")
            set_progress_bar_to_error(progress_bar)
        finally:
            progress_bar.setMaximum(100)  # Reset progress bar to determinate state

    def update_progress(block_num, block_size, total_size, progress_bar):
        read_data = block_num * block_size
        if total_size > 0:
            percent = int(read_data * 100 / total_size)
            progress_bar.setValue(percent)

    def set_progress_bar_to_error(progress_bar):
        progress_bar.setValue(100)
        progress_bar.setStyleSheet("QProgressBar::chunk {background-color: red;}")

    app = QApplication(sys.argv)

    window = QWidget()
    text_box = QLabel()
    progress_bar = QProgressBar()
    progress_bar.setAlignment(Qt.AlignCenter)
    button = QPushButton('检查更新')

    initUI(window, text_box, progress_bar, button)

    app.exec_()