import socket_library as sl
import time
import datetime

s = sl.server()


def main():
    BUFFERSIZE = 4096

    print("Running Server...")
    ip, port = s.establish_server_connection()
    while ip == 1 and port == 1:
        print("Error: Failed to establish server")
        reconnect_time = 3
        print("Retrying in " + str(reconnect_time) + " seconds...")
        time.sleep(reconnect_time)
        ip, port = s.establish_server_connection()

    print("Server Established at IP: " + str(ip) + " Port: " + str(port))
    print("Listening to calls")

    while 1:
        s.listen(5)
        conn, addr = s.accept()
        print("Connection Address:" + str(addr) + " " + str(datetime.datetime.now()))

        fp = open("./example/ship.zip", 'wb')
        while True:
            data = conn.recv(BUFFERSIZE)
            if not data:
                break
            fp.write(data)
        fp.close()
        conn.close()


if __name__ == "__main__":
    main()
