import socket_library as sl
import time
import datetime

MAX_CONNECTION = 5
BUFFER_SIZE = 4096


def setup():
    print("Starting Server...")
    ip, port = server.set_server_connection()
    while ip == 1 and port == 1:
        reconnect_time = 3
        print("Retrying in " + str(reconnect_time) + " seconds...")
        time.sleep(reconnect_time)
        ip, port = server.set_server_connection()

    print("Server Established at IP: " + str(ip) + " Port: " + str(port))
    print("Waiting for connections")

    while True:
        server.listen(MAX_CONNECTION)
        conn, addr = server.accept()
        print("Connection Address:" + str(addr) + " " + str(datetime.datetime.now()))
        server.echo_connection(conn, conn.recv(BUFFER_SIZE))
        conn.close()


if __name__ == "__main__":
    server = sl.Server()
    setup()

