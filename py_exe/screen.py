from pykeyboard import PyKeyboard
from pymouse import PyMouse
import time
import pyperclip


m = PyMouse()  # 建立鼠标对象
k = PyKeyboard()  # 建立键盘对象
time.sleep(2)
# ------------------------------------------
xy = m.position()  # 获取当前坐标的位置
print(xy)
m.click(xy[0], xy[1])  # 移动并且在(x,y)位置左击

# ------------------------------------------

k.type_string('123abc')

pyperclip.copy('输入中文')
k.press_key(k.control_key)  # 按下Ctrl键
k.tap_key('V')						# 点击V键
k.release_key(k.control_key)  # 松开Ctrl键
