import Lib.BotController as BotController
import Lib.EventManager
import Lib.QQRichText as QQRichText
import Lib.OnebotAPI as OnebotAPI
import Lib.MuRainLib as MuRainLib
import os
import Lib.Logger as Logger
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit, QMessageBox,QVBoxLayout
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
    import main
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