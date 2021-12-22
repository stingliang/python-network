# -*- coding: utf-8 -*-

# @File        : server.py
# @CreateDate  : 2021-12-22
# @Author      : stingliang
# @Github      : https://github.com/stingliang

import socket
import threading
from loguru import logger

CONTRAL_PORT = 6100
DATA_PORT = 6105
DATA_FILE = r'C:\Users\liangrui\PycharmProjects\python-network\sync\lidar.data'


def contral_server():
    s = socket.socket()
    host = socket.gethostname()
    s.bind((host, CONTRAL_PORT))
    s.listen(1)

    while True:
        c, addr = s.accept()
        command = c.recv(1024)
        logger.info('Got connection from: {}, received message: {}'.format(addr, str(command)))
        c.send(('This is the reply of the simulation script, your command: ' + str(command)).encode('utf-8'))
        c.close()


def data_server():
    s = socket.socket()
    host = socket.gethostname()
    s.bind((host, DATA_PORT))
    s.listen(1)

    while True:
        c, addr = s.accept()
        logger.info('Got connection from: ', addr)
        while True:
            with open(DATA_FILE, 'r') as f:
                linedata = f.readline()
                c.send(bytes(linedata))


def main():
    contral_thread = threading.Thread(target=contral_server)
    data_thread = threading.Thread(target=data_server)
    contral_thread.start()
    data_thread.start()
    contral_thread.join()
    data_thread.join()


if __name__ == '__main__':
    main()
