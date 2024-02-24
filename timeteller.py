# API service that returns current date and time in UTC or (optional) passed timezone

import socket

HOST = '127.0.0.1'
PORT = 13000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    