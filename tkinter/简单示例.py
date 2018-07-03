# -*- coding: utf-8 -*-
"""
@time:2018/5/25 20:39

@author: BX
"""
import tkinter
#创建主窗口
win=tkinter.Tk()
#设置标题
win.title('白雪')
#设置大小和位置
win.geometry('400x400+200+200')#距离左侧200，上边0，大小为400*400
#进入消息循环（即放置控件）
'''
label：标签控件，可以显示文本
'''
#win：父窗体，
#text:显示文本内容
#bg:背景色
#fg:字体颜色
#font：字体大小和字号
#wraplength:指定ttext文本中多宽进行换行
label=tkinter.Label(win,text='白雪是一个好人',\
                    bg='blue',fg='red',font=('宋体',20),\
                    width=20,height=2,wraplength=100)








#显示出来
label.pack()

win.mainloop()