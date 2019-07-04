import socket
import time
import os
import sys
import socket_wrapper as sl

reconnect_time = 3
BUFFER_SIZE = 4096

def setup():
    print("Starting client...")
    i = 0
    while client.set_client_connection():
        i += 1
        if i >= 5:
            print("Error: Timed out too many times")
            sys.exit()

        print("Retrying in " + str(reconnect_time) + " seconds...")
        time.sleep(reconnect_time)
        print("Starting client...")

    print("Client started")
    client.send_string(client.name + "///is online")
    client.confirm_connection()

def loop():
    while True:
        
        time.sleep(1)


if __name__ == "__main__":
    client = sl.Client()
    setup()
    loop()
    client.close()