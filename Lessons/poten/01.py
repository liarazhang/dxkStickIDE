# 电位器控制灯泡-改进1

# 硬件模块：
# micro:bit×1；主板×1
# 模块×2：电位器、LED灯泡

# 简介：
# 根据电位器读数设置LED灯泡状态
# 加入记录LED状态的变量以防止重复发出指令

import poten, led  # 导入模块控制库
from microbit import sleep

is_on = False  # 记录LED当前状态，防止重复操作
led.off()  # 确保初始LED为关闭状态

# 循环进行
while True:
    # 读取电位器位置（0-4095）
    pv = poten.value()

    # 根据读数设置LED灯状态
    if pv < 2048:
        if is_on:
            led.off()
            is_on = False
    elif not is_on:
        is_on = True
        led.on()

    # 等待0.2秒后进行下一次读数
    sleep(200)