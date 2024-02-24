"""API service that returns current date and time in UTC or (optional) passed timezone"""

import socket
import json
from datetime import datetime, timezone, timedelta

def get_utc_time() -> object:
    """
    Returns current time in UTC

    :return: current UTC time object
    """
    return datetime.now(timezone.utc)

def get_adjusted_time(tz_offset) -> object:
    """
    Returns current time in passed timezone offset

    :param tz_offset: integer of timezone offset from UTC
    
    :return: current time object
    """
    tz = timezone(timedelta(hours=float(tz_offset)))
    adjusted_time = get_utc_time().astimezone(tz)
    return adjusted_time

def format_time(time_obj, tz_offset) -> dict:
    """
    Converts time object to dictionary for response to client

    :param time_obj: time object from datetime
    :param tz_offset: timezone offset from UTC

    :return: dictionary of values
    """
    return {
        "year": time_obj.year,
        "month": time_obj.month,
        "day": time_obj.day,
        "hour": time_obj.hour,
        "minute": time_obj.minute,
        "second": time_obj.second,
        "UTC_offset": tz_offset
    }

def process_client(client_socket):
    """
    Receives client request and sends timestamp
    
    :param client_socket: the client socket
    """
    # format client data as integer
    data = client_socket.recv(1024).decode("utf-8").strip()
    adjusted_time = get_adjusted_time(data)
    print(f"Received '{data}'")
    response = format_time(adjusted_time, data)
    print(f"Sending '{response}'")
    client_socket.send(json.dumps(response).encode("utf-8"))

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
