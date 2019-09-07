from tkinter import *
from 百度 import search
from 堆糖 import sugar



root = Tk()

Label(root,text='请输入要寻找的关键词:').grid(row=0,column=0)
Label(root,text='请输入要想要在桌面创建的文件名:').grid(row=1,column=0)

v1 = StringVar()
v2 = StringVar()



e1 = Entry(root,textvariable=v1)
e2 = Entry(root,textvariable=v2)
e1.grid(row=0,column=1,padx=10,pady=5)
e2.grid(row=1,column=1,padx=10,pady=5)

def llrt():
    search(e1.get(),e2.get())

def llrt1():
    sugar(e1.get(),e2.get())


Button(root,text='百度下载',width=0,command=llrt).grid(row=3,column=0,pady=5,sticky=W)

Button(root,text='退出',width=0,command=root.quit).grid(row=3,column=2,pady=5,sticky=E)

Button(root,text='堆糖下载',width=0,command=llrt1).grid(row=3,column=1,padx=0,pady=5,sticky=W)

    

mainloop()
