import socket

s = socket

def main():
    print("Sending File...")
    establish_tcp_connection()

def establish_tcp_connection(local_ip= "192.168.1.118", local_port = 6815):
    BUFFERSIZE = 1024
    MESSAGE = "Hello, World!"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(local_ip, local_port)
    s.send(MESSAGE)
    s.close()




if __name__ == "__main__":
    main()



