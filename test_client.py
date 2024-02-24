"""Simple client used to test miroservice"""

import socket

HOST = "127.0.0.1"
PORT = 13000
COUNT = 5

for i in range(COUNT):
    timezone = input("enter integer in range [-12 ... 14]: ")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(timezone.encode("utf-8"))
        data = s.recv(1024)
        print(f"Received {data!r}")
