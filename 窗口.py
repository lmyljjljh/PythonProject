import tkinter
from tkinter import ttk


# 命名窗口对象
win = tkinter.Tk()
frm = ttk.Frame(win, padding=10)
frm.grid()


# 窗口属性的设置
win.title("示例")
win.geometry("1000x600+200+500")


# win.geometry(“axb+c+d”)
# 参数 a 是指窗口的宽度（(横向长度），参数 b 是窗口的高度（纵向长度）
# 参数 c 和 d 是窗口左上点距离屏幕最左上点的距离
# c 是横向距离，d 是纵向距离

# 函数
def func():
    # print("你好")
    ttk.Label(frm, text="hello word!").grid(column=0, row=0)
    # grid()方法被用来指明标签在包含它的框架控件中的相对布局（定位），作用类似于HTML中的表格。

# 按钮设置
button = tkinter.Button(win, text="按钮", width=30, height=3, command=func)
button.place(x=10, y=320)

# PS：按钮的width和height是以文本字符为大小的
# tkinter.Button(A,text=“B”,width = C , height = D ,command = E)
# 如上所示的例子中：
# A：窗口对象的名称
# B：按钮的名称
# C：宽度，横向长度
# D：高度，纵向长度
# E：本案例中是命名了一个函数 func() ，然后执行函数中的代码，也可以直接设置成简单的函数
#
# botton.place(x= a , y= b)
# a：距离窗口界面左上点的横向距离
# b：距离窗口界面左上点的纵向距离

ttk.Button(frm, text="Quit", command=win.destroy).grid(column=1, row=0)

# 窗口显示
win.mainloop()
