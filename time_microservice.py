"""API service that returns current date and time in UTC or (optional) passed timezone"""

import socket

def main():
    host = '127.0.0.1'
    port = 13000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Listening on {host}:{port}...")
    
    connection, address = server_socket.accept()
    with connection:
        print(f"Connection from {address}")
        while True:
            data = connection.recv(1024)
            if not data:
                break
            connection.sendall(data)
