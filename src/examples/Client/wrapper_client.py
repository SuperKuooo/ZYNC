import time
import threading
import sys, os; sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'\\File Transfer')
import lib.socket_wrapper as sw

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
        op = client.recv(BUFFER_SIZE)
        print(op)
        if op == bytes('0', 'utf-8'):
            client.send_string(op, True)
        elif op == bytes('zip', 'utf-8'):
            fp = open('../save/shipment.zip', 'wb')
            client.save_file(BUFFER_SIZE, fp)
        elif op == 'image':
            fp = open('../save/shipment.img', 'wb')
            # client.save_file(BUFFER_SIZE, fp)
        elif op == 'break':
            raise KeyboardInterrupt
        time.sleep(0.5)

def alive_message_loop():
    while True:
        pass


if __name__ == '__main__':
    client = sw.Client()
    setup('192.168.1.118', 8000)
    t1 = threading.Thread(target=communication_loop, name='communication_loop')
    t2 = threading.Thread(target=alive_message_loop(), name='alive_message_loop')

    try:
        t1.start()
        # t2.start()
    except KeyboardInterrupt:
        t1.join()
        # t2.join()
        client.close()
