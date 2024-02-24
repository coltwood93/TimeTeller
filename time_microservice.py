"""API service that returns current date and time in UTC or (optional) passed timezone"""

import socket

def process_client(client_socket):
    """Receives client request and sends timestamp"""
    # format client data as integer
    data = client_socket.recv(1024).decode("utf-8").strip()
    print(f"Received '{data}'")
    print(f"Sending '{data}'")
    client_socket.sendall(data.encode("utf-8"))

def main():
    """Main function to create server socket and listen for client connections"""
    host = '127.0.0.1'  # set for running locally
    port = 13000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))    # initialize socket
    server_socket.listen()
    print(f"Listening on {host}:{port}...")
    while True:
        client_socket, addr = server_socket.accept()    # accept client connection
        print(f"Connection from {addr}")
        process_client(client_socket)    # process client request

if __name__ == "__main__":
    main()
