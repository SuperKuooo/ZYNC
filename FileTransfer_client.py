import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def main():
    print("Initializing...")
    while establish_tcp_connection():
        reconnect_time = 3
        print("Retrying in " + str(reconnect_time) + " seconds...")
        time.sleep(reconnect_time)

    send_file()
    s.close()
    return 0

def establish_tcp_connection(TCP_IP= "192.168.1.97", TCP_PORT = 8000):
    #BUFFERSIZE = 1024
    try:
        s.connect((TCP_IP, TCP_PORT))
    except:
        print("Error: Failed to establish connection")
        return 1
   
    print("Connection Established")
    return 0

def send_file():
    MESSAGE = "Hello, World!"
    b = bytes(MESSAGE, "utf-8")
    s.send(b)
    try:
        s.send(MESSAGE)
    except:
        print("Error: Failed to send message")
        return 1
    
    print("Message Sent!")
    return 0

if __name__ == "__main__":

