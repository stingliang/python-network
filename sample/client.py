# -*- coding: utf-8 -*-

# @File        : client.py
# @CreateDate  : 2021-12-22
# @Author      : stingliang
# @Github      : https://github.com/stingliang

import socket
import time
from loguru import logger

CONTRAL_PORT = 6100
DATA_PORT = 6105


def send_command(command):
    s = socket.socket()
    host = socket.gethostname()
    s.connect((host, CONTRAL_PORT))
    s.send(command.encode('utf-8'))
    time.sleep(0.1)
    logger.info('Receive: ', s.recv(1024))
    s.close()


if __name__ == '__main__':
    while True:
        input_str = input("Input command: ")
        send_command(str(input_str))
