# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 10:03:50 2020

@author: Abdullah
"""

import socket

host = '127.0.0.1'
port = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen()
conn, addr = s.accept()

with conn:
    print("Connected by", addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)