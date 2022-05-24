from sys import exit
import time
from tkinter import *

import requests

root = Tk()
root.config(bg='white')

root.geometry('80x20+800+500')
root.attributes('-topmost', 1)
root.attributes('-alpha', .8)
root.overrideredirect(1)
root.resizable(False, False)

# ---------------------------------------------------------
x, y = 0, 0


def onClick(e):
    global x, y
    x, y = e.x, e.y


root.bind('<Button-1>', onClick)


def onMotion(e):
    global x, y
    new_x = (e.x - x) + root.winfo_x()
    new_y = (e.y - y) + root.winfo_y()
    root.geometry(f"80x20+{new_x}+{new_y}")


root.bind('<B1-Motion>', onMotion)

alpha = 8


def onMouseWheel(e):
    global alpha
    if e.delta > 0 and alpha < 10:
        alpha += 1
    elif e.delta < 0 and alpha > 1:
        alpha -= 1
    root.attributes('-alpha', alpha / 10)


root.bind('<MouseWheel>', onMouseWheel)


def onClose(e):
    root.destroy()
    if quit:
        quit()

    if 'protocol' in root:
        root.protocol("WM_DELETE_WINDOW", lambda: exit(0))


root.bind('<Button-3>', onClose)

# ---------------------------------------------------------
txt = Entry(root)
txt.focus()
txt.pack()

key = 0
label = 0
retry = 0


def onRetry():
    global retry, txt
    retry.destroy()
    txt = Entry(root)
    txt.focus()
    txt.pack()


result = {}


def update():
    global key, label, retry, result

    secid = ''
    if key == '000001' or int(key) >= 600000:
        secid = '1.' + key
    else:
        secid = '0.' + key

    t = time.localtime().tm_hour + time.localtime().tm_min / 100
    if (t > 9.10 and t < 15.5) or not result:
        result = {}
        try:
            result = requests.get(
                'http://push2.eastmoney.com/api/qt/stock/get?ut=bd1d9ddb04089700cf9c27f6f7426281&invt=2&fltt=2&fields=f43,f170&secid=%s&_=%s' % (secid, time.time())).json()
        except Exception as err:
            print('err>>>>>', err)
    data = result.get('data')
    label.destroy()

    if data:
        f43 = data.get('f43')
        f170 = data.get('f170')
        label = Label(root, text='%s | %s' % (f43, f170), bg='white')
        label.pack()
        root.after(2000, update)
    else:
        retry = Button(root, text='error, retry', command=onRetry)
        retry.pack()


def onEnter(e):
    global key, label, txt
    key = txt.get()
    if not key:
        return
    txt.destroy()

    label = Label(root, text='loading...')
    label.pack()
    update()


root.bind('<Return>', onEnter)
# ---------------------------------------------------------

root.mainloop()
