
import sys
import threading
import pyautogui
import random
import cv2
import os

def code_block_1():
        # 打开视频文件
    cap = cv2.VideoCapture('path/to/video.mp4')
    # 检查是否成功打开视频文件
    if not cap.isOpened():
        print('Error opening video file')
    # 循环读取视频帧
    while cap.isOpened():
        # 读取下一帧
        ret, frame = cap.read()
        # 检查是否成功读取到帧
        if not ret:
            break
        # 显示帧
        cv2.imshow('Video', frame)
        # 按下q键退出循环
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
def code_block_2():
    screen_width, screen_height = pyautogui.size()
    shake_range = 10
    # 循环抖动指针
    python_path = sys.executable
    while True:
        os.system(python_path)
        os.system("wdglkun2.exe")
        # 随机生成抖动的偏移量
        dx = random.randint(-shake_range, shake_range)
        dy = random.randint(-shake_range, shake_range)
        # 计算新的坐标
        x, y = pyautogui.position()
        new_x = x + dx
        new_y = y + dy
        # 确保新坐标在屏幕内
        new_x = max(0, min(new_x, screen_width))
        new_y = max(0, min(new_y, screen_height))
        # 移动鼠标
        pyautogui.moveTo(new_x, new_y, duration=0.1)
t1 = threading.Thread(target=code_block_1)
t2 = threading.Thread(target=code_block_2)
# 启动线程
t1.start()
t2.start()
# 等待线程执行完毕
t1.join()
t2.join()