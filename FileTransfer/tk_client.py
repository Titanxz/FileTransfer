#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   {Titanxz}
# @Time    :   2019/8/27 17:53
# @License :   (C) Copyright 2019, {python_1904}


from tkinter import *
from socket import *


def client():
    ip = IP.get()
    port = int(Port.get())
    buf_size = 1024
    address = (ip, port)
    tcp_client_socket = socket(AF_INET, SOCK_STREAM)
    tcp_client_socket.connect(address)

    file = open('P(1).jpg', 'wb')
    while 1:
        image_data = tcp_client_socket.recv(buf_size)
        if not image_data:
            print('数据读取完毕...')
            break
        file.write(image_data)
    tcp_client_socket.close()


win = Tk()
win.title('FileTransfer1.0')
win.iconbitmap('software.ico')
win.geometry('300x150+500+300')
win.attributes('-alpha', 1)
win.configure(background='white')
win.resizable(0, 0)
IP = StringVar(win, '')
Port = StringVar(win, '')
label1 = Label(win, text='IP', font=('黑体', 14), bg='white', fg='black').place(relx=0.1, rely=0.15)
label2 = Label(win, text='Port', font=('黑体', 14), bg='white', fg='black').place(relx=0.1, rely=0.35)
entry1 = Entry(win, textvariable=IP, bd=10, width=25).place(relx=0.3, rely=0.1)
entry2 = Entry(win, textvariable=Port, bd=10, width=25).place(relx=0.3, rely=0.3)
button1 = Button(win, text='接受', command=client, width=5, font=('黑体', 14)).place(relx=0.3, rely=0.7)
button2 = Button(win, text='退出', width=5, command=win.quit, font=('黑体', 14)).place(relx=0.6, rely=0.7)
win.mainloop()
