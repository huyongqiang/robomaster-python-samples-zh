def start():
    云台.俯仰(30)
    云台.俯仰(-10)

# 以下为API中文化部分, 与程序逻辑无关. 请勿作修改.

云台 = gimbal_ctrl
云台.俯仰 = 云台.pitch_ctrl
