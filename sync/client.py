
# -*- coding: utf-8 -*-

# @File        : client.py
# @CreateDate  : 2021-12-22
# @Author      : stingliang
# @Github      : https://github.com/stingliang

import socket

SAMPLE_PORT = 1234

s = socket.socket()
host = socket.gethostname()
s.connect((host, SAMPLE_PORT))
print('Reply: ', s.recv(1024))
