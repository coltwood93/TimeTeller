"""Simple client used to test miroservice"""

import socket

HOST = "127.0.0.1"
PORT = 13000
TIMEZONE = str(-7)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(TIMEZONE.encode("utf-8"))
    data = s.recv(1024)

print(f"Received {data!r}")
