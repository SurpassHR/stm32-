# coding = utf-8
import re
import os
import itchat
import pyautogui
import time

d = os.path.dirname(__file__)  # 文件路径
parent_path = os.path.dirname(d)  # 相对路径

# 快捷方式
prog_dict = {
        'p': r'{}/Proteus 8 Professional.lnk'.format(parent_path),
        'k': r'{}/Keil5/led.uvprojx'.format(parent_path),
        'porthelper': r'{}/PortHelper.exe'.format(parent_path),
        'wt': r'C:\Users\胡睿\AppData\Local\Microsoft\WindowsApps\wt.exe'
    }

# 快捷操作
operation_dict = {
        'shutdown1':'shutdown /l',
        'shutdown2':'shutdown /s'
    }

# 指南
fh_help = '''------------------
Maybe you want...
serial 参数 --> 单次串口通信
serial 0 --> 仿真功能
p --> Proteus
file --> 打开文件
start --> 开始proteus仿真
stop --> 停止仿真
open --> 快捷方式
wt --> windows terminal(自定义)
command --> 操作指令(自定义)
------------------
'''
oper_help = '''------------------
Command list
shutdown1 --> 注销
shutdown2 --> 关机
------------------
'''
print_list = '''------------------
Supported progam
p --> Proteus
k --> Keil5
porthelper-->porthelper
------------------
'''

# 文件助手
def filehelper(msg): # 文件助手作为主菜单
    if msg['Text'] == 'help':
        itchat.send_msg(fh_help, toUserName='filehelper')
    elif msg['Text'] == 'open':
        itchat.send_msg(print_list, toUserName='filehelper')
    elif msg['Text'] == 'command':
        itchat.send_msg(oper_help, toUserName='filehelper')
    elif msg['Text'] == 'serial 0':
        itchat.send_msg('T for Temperature\nS for Distance\n0 for Stop', toUserName='filehelper')
        itchat.send_msg('Press button to control:\nKEY0 只亮LED0\nKEY1 全部熄灭\nKEY2 不断的循环流水灯KEY3 切换不断循环的流水灯的方向\nKEY4 获取超声波数据，显示在虚拟终端，距离小于100cm，蜂鸣器报警\nKEY5 获取温湿度数据，显示在虚拟终端，温度高于30℃或湿度大于60%，蜂鸣器报警', toUserName='filehelper')
    elif re.split(' ', msg['Text'])[0] == 'serial':  # 启用串口通信功能
        ret_info = serial_send_data(re.split(' ', msg['Text'])[1])
        itchat.send_msg(ret_info, toUserName='filehelper')
    elif msg['Text'] in prog_dict.keys():  # 如果命令包含在可操作性程序列表中
        open_prog(msg['Text'])
        itchat.send_msg('programe opened', toUserName='filehelper')
    elif msg['Text'] in operation_dict.keys():  # 如果是可执行操作
        oper_sys(msg['Text'])
    elif msg['Text'] == 'start':
        pyautogui.moveTo(30, 1027, duration=0.5)
        pyautogui.click(clicks=1, button='left', interval=0.0)
        itchat.send_msg('simulation started', toUserName='filehelper')
    elif msg['Text'] == 'stop':
        pyautogui.moveTo(1954, 818, duration=0.5)
        pyautogui.click(clicks=1, button='left', interval=0.0)
        itchat.send_msg('programe stopped', toUserName='filehelper')
    elif msg['Text'] == 'file':
        pyautogui.moveTo(588, 270, duration=0.5)
        pyautogui.click(clicks=1, button='left', interval=0.0)
        itchat.send_msg('file opened', toUserName='filehelper')
    else:
        itchat.send_msg('filehelper没有此命令！', toUserName='filehelper')

# 监听消息
@itchat.msg_register(itchat.content.TEXT)
def core_func(msg):
    AdminUserName = itchat.get_friends()[0]['UserName'] # 每次刷新本账号的用户代码
    Name = []
    username = msg['FromUserName'] # 收到的消息的发送者
    # print(username) # √ 独一无二代码
    remarkname = itchat.search_friends(userName=username)['RemarkName']
    # print(remarkname) # √ 备注
    nickname = itchat.search_friends(userName=username)['NickName']
    # print(nickname) # √ 昵称，自起
    Name.append(nickname)
    Name.append(remarkname)
    if msg['ToUserName'] == 'filehelper':
        filehelper(msg)
    else:
        return None

# 串口通信
def serial_send_data(send):
    import serial

    # 连接串口
    serial = serial.Serial('COM1', 9600, timeout=2) # 端口号, 波特率, 超时
    if serial.isOpen():
        print('串口已打开')
        send = send.upper()  # 便于识别全部转换为大写
        send = str.encode(send)  # str转bytes
        # print('You Send Data:', msg)
        serial.write(send)  # 串口写数据

        while True:
            data = serial.read(40)  # 串口读200位数据
            time.sleep(0.5)
            break
        data = bytes.decode(data)
        data = re.findall('\n\r(.*)\n\r', data)
        if (re.findall('Temperature', data[0])):
            data[0] = data[0]+'℃'
        print('receive data is :', data[0])
        return data[0]

# 打开路径
def open_prog(path):
    os.startfile(prog_dict[path])

# 执行操作
def oper_sys(operation):
    print(operation_dict[operation])
    os.system(operation_dict[operation])

# 入口
if __name__ == '__main__':

    itchat.auto_login()
    itchat.run()

