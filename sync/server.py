
# -*- coding: utf-8 -*-

# @File        : server.py
# @CreateDate  : 2021-12-22
# @Author      : stingliang
# @Github      : https://github.com/stingliang

import socket

SAMPLE_PORT = 1234

s = socket.socket()
host = socket.gethostname()
s.bind((host, SAMPLE_PORT))
s.listen(5)

while True:

    c, addr = s.accept()
    print('Got connection from: ', addr)
    c.send(b'Thank you for connecting')
    c.close()
    pass
