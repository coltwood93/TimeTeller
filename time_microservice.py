"""API service that returns current date and time in UTC or (optional) passed timezone"""

import socket

def main():
    """listens for client connection and processes incoming traffic"""
    host = '127.0.0.1'
    port = 13000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Listening on {host}:{port}...")
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        with client_socket:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                print(f"Received {data}")
                client_socket.sendall(data)

if __name__ == "__main__":
    main()
