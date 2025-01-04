import Lib.BotController as BotController
import Lib.EventManager
import Lib.QQRichText as QQRichText
import Lib.OnebotAPI as OnebotAPI
import Lib.MuRainLib as MuRainLib
import os,threading
import Lib.Logger as Logger
import Lib.GUILib as GUILib

logger = Logger.logger

commands = []


class CommandParsing:
    def __init__(self, input_command: str):
        self.input_command = input_command
        self.command = None
        self.command_args = None
        self.command_list = self.parse()
        self.command = self.command_list[0]
        self.command_args = [_ for _ in self.command_list[1:] if isinstance(_, str)] \
            if len([_ for _ in self.command_list if isinstance(_, str)]) > 1 else []
        self.command_kwargs = {
            k: v for d in [_ for _ in self.command_list if isinstance(_, dict)] for k, v in d.items()
        }

    def parse(self):
        flag = True
        is_in_quote = False
        now_quote_type = None
        is_escape = False
        counter = 0
        command_list = []
        now_command = ""
        for s in self.input_command:
            if s == "\\" and not is_escape:
                is_escape = True
            elif s == "\\" and is_escape:
                now_command += s
                is_escape = False
            elif s == '"' and now_quote_type != "'" and not is_escape:
                is_in_quote = not is_in_quote
                now_quote_type = '"' if is_in_quote else None
            elif s == '"' and now_quote_type != "'" and is_escape:
                now_command += s
                is_escape = False
            elif s == "'" and now_quote_type != '"' and not is_escape:
                is_in_quote = not is_in_quote
                now_quote_type = "'" if is_in_quote else None
            elif s == "'" and now_quote_type != '"' and is_escape:
                now_command += s
                is_escape = False
            elif s == ' ' and not is_in_quote:
                if flag:
                    if "=" in now_command:
                        now_command = now_command.split("=")
                        if len(now_command) == 2:
                            command_list.append({now_command[0]: now_command[1]})
                        else:
                            raise Exception("命令格式错误")
                    else:
                        command_list.append(now_command)
                    now_command = ""
                else:
                    flag = True
                counter += 1
            else:
                now_command += s

        if flag:
            if "=" in now_command:
                now_command = now_command.split("=")
                if len(now_command) == 2:
                    command_list.append({now_command[0]: now_command[1]})
                else:
                    raise Exception("命令格式错误")
            else:
                command_list.append(now_command)
        return command_list


class Meta(type):
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        if 'Command' in globals() and issubclass(cls, Command):
            commands.append(cls())  # 将子类添加到全局列表中


class Command(metaclass=Meta):
    def __init__(self):
        self.command_help = ""  # 命令帮助
        self.need_args = None  # 需要的参数(None即不需要)
        self.command_name = ""  # 命令名
        """
        need_args = {
            "arg1": {  # 参数名
                "type": int,  # 类型
                "help": "参数1的帮助信息",  # 参数帮助信息
                "default": 0  # 默认值
                "must": True  # 是否必要   
            }
        """

    def run(self, input_command: CommandParsing, kwargs):
        # 执行命令
        pass


class SendGroupMsgCommand(Command):
    def __init__(self):
        super().__init__()
        self.command_help = "SEND_GROUP_MSG: 发送消息到群"
        self.command_name = "SEND_GROUP_MSG"

    def run(self, input_command: CommandParsing, kwargs):
        GUILib.SEND_MSG_TO_GROUP()


class SendMsgCommand(Command):
    def __init__(self):
        super().__init__()
        self.command_help = "SEND_MSG: 发送消息到好友"
        self.command_name = "SEND_MSG"

    def run(self, input_command: CommandParsing,kwargs):
        GUILib.SEND_MSG_TO_USER()
        

class ExitCommand(Command):
    def __init__(self):
        super().__init__()
        self.command_help = "EXIT: 退出程序"
        self.command_name = "EXIT"

    def run(self, input_command: CommandParsing, kwargs):
        MuRainLib.finalize_and_cleanup()

class AboutCommand(Command):
    def __init__(self):
        super().__init__()
        self.command_help = "ABOUT: 关于"
        self.command_name = "ABOUT"

    def run(self, input_command: CommandParsing, kwargs):
        GUILib.ABOUT()

class UpdateCheckCommand(Command):
    def __init__(self):
        super().__init__()
        self.command_help = "UPDATE_CHECK: 检查更新"
        self.command_name = "UPDATE_CHECK"

    def run(self, input_command: CommandParsing, kwargs):
        GUILib.UPDATE()




class RunAPICommand(Command):
    def __init__(self):
        super().__init__()
        self.command_help = "RUN_API: 运行API"
        self.command_name = "RUN_API"
        self.api = OnebotAPI.OnebotAPI(original=True)

    def run(self, input_command: CommandParsing, kwargs):
        try:
            import tkinter
            window = tkinter.Tk()
            window.title("运行API")
            window.geometry("300x120")
            lbl = tkinter.Label(window, text="API节点",font=("Arial", 12))
            lbl.grid(column=0, row=0)
            lbl1 = tkinter.Label(window, text="参数（可选）",font=("Arial", 12))
            lbl1.grid(column=0, row=2)
            Point = tkinter.Entry(window, width=15,font=("Arial", 12))
            Point.grid(column=1, row=0)
            More = tkinter.Entry(window, width=15,font=("Arial", 12))
            More.grid(column=1, row=2)
            def clicked():        
                api_name = tkinter.Entry.get(Point)
                api_params = tkinter.Entry.get(More)
                logger.debug(f"API: {api_name}, 参数: {api_params}")
                print(self.api.get(api_name, api_params)[1].json())
                window.destroy()
            btn = tkinter.Button(window, text="运行", command=clicked,font=("Arial", 12))
            btn.grid(column=3, row=3)
            window.mainloop()
        except:
            logger.error("弹出窗口异常")


class HelpCommand(Command):
    def __init__(self):
        super().__init__()
        self.command_help = "help: 查看帮助"
        self.command_name = "help"

    def run(self, input_command: CommandParsing, kwargs):
        help_text = "命令帮助：\n" + "\n".join([command.command_help for command in commands])
        print(help_text)


def run_command(input_command):
    try:
        run_command = None
        for command in commands:
            if input_command.command == command.command_name:
                run_command: Command = command
                break
    except Exception as e:
        logger.error(f"检查命令时发生错误: {e}")
        return
    if run_command is not None:
        try:
            kwargs = {}
            if run_command.need_args is not None and len(run_command.need_args) > 0:
                n = len(input_command.command_args)
                counter = len(
                    [arg_name for arg_name, arg_info in run_command.need_args.items() if arg_info["must"]])
                for arg_name, arg_info in run_command.need_args.items():
                    if n == 0:
                        break
                    if arg_info["must"]:
                        kwargs[arg_name] = input_command.command_args.pop(0)
                        if arg_info["type"] == int:
                            kwargs[arg_name] = int(kwargs[arg_name])
                        elif arg_info["type"] == float:
                            kwargs[arg_name] = float(kwargs[arg_name])
                        elif arg_info["type"] == bool:
                            kwargs[arg_name] = bool(kwargs[arg_name])
                        elif arg_info["type"] == dict or arg_info["type"] == list or arg_info["type"] == tuple:
                            kwargs[arg_name] = eval(kwargs[arg_name])
                        n -= 1
                        counter -= 1
                    else:
                        kwargs[arg_name] = arg_info["default"]

                for arg_name, arg_info in input_command.command_kwargs.items():
                    if arg_name in [_arg_name for _arg_name, _arg_info in run_command.need_args.items()]:
                        if arg_name not in kwargs:
                            counter -= 1
                        kwargs[arg_name] = arg_info
                        arg_type = run_command.need_args[arg_name]["type"]
                        if arg_type == int:
                            kwargs[arg_name] = int(kwargs[arg_name])
                        elif arg_type == float:
                            kwargs[arg_name] = float(kwargs[arg_name])
                        elif arg_type == bool:
                            kwargs[arg_name] = bool(kwargs[arg_name])
                        elif arg_type == dict or arg_info["type"] == list or arg_info["type"] == tuple:
                            kwargs[arg_name] = eval(kwargs[arg_name])

                if counter > 0:
                    raise Exception("缺少参数")

            run_command.run(input_command, kwargs)
        except Exception as e:
            logger.error(f"执行命令时发生错误: {repr(e)}")
    else:
        logger.error("未知的命令, 请发送help查看支持的命令")


def listening_command():
    while True:
        try:
            input_command = input()
        except (KeyboardInterrupt, EOFError, UnicodeDecodeError):
            MuRainLib.finalize_and_cleanup()
            return
        except Exception as e:
            logger.error(f"输入命令时发生错误: {repr(e)}")
            continue

        if len(input_command) == 0:
            continue

        if input_command[0] == "/":
            input_command = input_command[1:]
        input_command = CommandParsing(input_command)
        run_command(input_command)
        logger.debug(f"Command: {input_command.command_list}")


def start_command_listener():
    import threading

    threading.Thread(target=listening_command, daemon=True).start()


if __name__ == "__main__":
    listening_command()
