import socket_library as sl
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import logging
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

    logging.basicConfig(filename="test.log",
                        level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = "C:/Users/user/Desktop/junk"
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    print("Server Established at IP: " + str(ip) + " Port: " + str(port))
    print("Waiting for connections")

def loop():
    try:
        while True:
            server.listen(MAX_CONNECTION)
            conn, addr = server.accept()
            print("Connection Address:" + str(addr) + " " + str(datetime.datetime.now()))
            server.echo_connection(conn, conn.recv(BUFFER_SIZE))
            conn.close()
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        server.close()    

if __name__ == "__main__":
    server = sl.Server()
    setup()
    loop()

