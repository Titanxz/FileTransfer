#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   {Titanxz}
# @Time    :   2019/8/27 16:09
# @License :   (C) Copyright 2019, {python_1904}


from tkinter import *
from socket import *


def server():
    ip = var_ip.get()
    port = int(var_port.get())
    buf_size = 1024
    address = (ip, port)
    tcp_server_socket = socket(AF_INET, SOCK_STREAM)
    tcp_server_socket.bind(address)
    tcp_server_socket.listen(5)

    while 1:
        file = open('p(0).jpg', 'rb')
        print('等待客户端的连接...')
        client_socket, client_address = tcp_server_socket.accept()
        print('来自%s的连接...' % str(client_address))
        image_data = file.read()
        if not image_data:
            continue
        client_socket.send(image_data)
        print('数据传输完毕...')
        client_socket.close()
    tcp_server_socket.close()


win = Tk()
win.title('FileTransfer1.0')
win.iconbitmap('software.ico')
win.geometry('300x150+500+300')
win.attributes('-alpha', 1)
win.configure(background='white')
win.resizable(0, 0)
var_ip = StringVar(win, '')
var_port = StringVar(win, '')
label1 = Label(win, text='IP', font=('黑体', 14), bg='white', fg='black').place(relx=0.1, rely=0.15)
label2 = Label(win, text='Port', font=('黑体', 14), bg='white', fg='black').place(relx=0.1, rely=0.35)
entry1 = Entry(win, textvariable=var_ip, bd=10, width=25).place(relx=0.3, rely=0.1)
entry2 = Entry(win, textvariable=var_port, bd=10, width=25).place(relx=0.3, rely=0.3)
button1 = Button(win, text='发送', width=5, command=server, font=('黑体', 14)).place(relx=0.3, rely=0.7)
button2 = Button(win, text='退出', width=5, command=win.quit, font=('黑体', 14)).place(relx=0.6, rely=0.7)
win.mainloop()
