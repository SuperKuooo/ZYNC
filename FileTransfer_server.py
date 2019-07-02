import socket_library as sl
import time

s = sl.server()

def main():
    print("Initializing...")

    while s.establish_server_connection():
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

if __name__ == "__main__":
    main()
