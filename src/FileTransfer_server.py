import threading
import socket_wrapper as sw
import logging
import time
import datetime

# Helpful command
# python generate_log_script.py univrse-Windows ./Univrse-Core/Windows/

MAX_CONNECTION = 5
BUFFER_SIZE = 4096
LIB_PATH = 'C:/Users/user/Documents/Unity_Build_Library'
TARGET_PATH = 'Univrse-Core/Windows'


def setup():
    print("Setting Server...")
    ip, port = server.set_server_connection(
        '192.168.1.118', attempt_to_reconnect=3)
    print("Server set at IP: " + str(ip) + " Port: " + str(port))
    print("Watchdog observer start")
    observer.start_observe(False)
    print("Waiting for connections...")


def connection_loop():
    while True:
        server.listen(MAX_CONNECTION)
        conn, addr = server.accept()
        print("Connection Address:" + str(addr) +
              " " + str(datetime.datetime.now()))
        server.echo_connection(conn, conn.recv(BUFFER_SIZE))


def communication_loop():
    while True:
        pass


def alive_message_loop():
    while True:
        sw.check_connection(server.get_list_of_connection())
        time.sleep(0.05)


if __name__ == "__main__":
    server = sw.Server()
    observer = sw.Observer(server, LIB_PATH, TARGET_PATH)
    t1 = threading.Thread(target=connection_loop, name='connection_loop')
    t2 = threading.Thread(target=communication_loop, name='communication_loop')
    t3 = threading.Thread(target=alive_message_loop, name='alive_message_loop')
    setup()

    try:
        t1.start()
        t2.start()
    except KeyboardInterrupt:
        t1.join()
        t2.join()
        observer.close()
        server.close()
