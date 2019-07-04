import time
import threading
import sys
import socket_library as sl

reconnect_time = 3
BUFFER_SIZE = 4096


def setup(ip, port):
    print("Starting client...")
    client.set_client_connection(ip, port, 5)
    print("Client started")
    client.send_string(client.get_client_name() + "///is online")
    client.confirm_connection()


def communication_loop():
    while True:
        type = client.recv(BUFFER_SIZE)
        print(type)
        if type == 'zip':
            fp = open('./save/shipment.zip', 'wb')
            # client.save_file(BUFFER_SIZE, fp)
        elif type == 'image':
            fp = open('./save/shipment.img', 'wb')
            # client.save_file(BUFFER_SIZE, fp)


def alive_message_loop():
    while True:
        pass




if __name__ == "__main__":
    client = sl.Client()
    setup('192.168.1.118', 8000)
    t1 = threading.Thread(target=communication_loop(), name='communication_loop')
    t2 = threading.Thread(target=alive_message_loop(), name='alive_message_loop')

    try:
        t1.start()
        t2.start()
    except KeyboardInterrupt:
        t1.join()
        t2.join()
        client.close()
