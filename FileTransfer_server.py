import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def main():
    print("Initializing...")

    while establish_tcp_connection():
        reconnect_time = 3
        print("Retrying in " + str(reconnect_time) + " seconds...")
        time.sleep(reconnect_time)

    BUFFERSIZE = 1024
    s.listen(1)

    conn, addr = s.accept()

    print("Connection Address:" + str(addr))
    while 1:
        data = conn.recv(BUFFERSIZE)
        if not data:
            break
        print("Received Data: ", data)

    conn.close()


def establish_tcp_connection(TCP_IP="192.168.1.97", TCP_PORT=8000):
    # BUFFERSIZE = 1024
    s.bind((TCP_IP, TCP_PORT))

    try:
        print(" ")
        # s.bind((TCP_IP, TCP_PORT))
    except socket.error:
        print("Error: Failed to establish connection")
        return 1

    print("Connection Established")
    return 0


if __name__ == "__main__":
    main()
