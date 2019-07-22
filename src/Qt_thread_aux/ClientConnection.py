from PyQt5 import QtCore
import threading
import os
from socket_wrapper.utils import *


class ClientConnectionThread(QtCore.QObject):
    sig = QtCore.pyqtSignal()

    def __init__(self, client, input_ip=None, input_port=None, buffer_size=4096, reconnect_time=3):
        # Initializing Vairables
        super(ClientConnectionThread, self).__init__()
        self.client = client
        self.messages = []
        self.SAVE_LOCATION = '..\\..\\save'
        self.run = False
        self.com_standby = True
        self.con_standby = True
        self.buffer_size = buffer_size
        self.input_ip = input_ip
        self.input_port = input_port
        self.reconnect_time = reconnect_time

        # Initializing threads
        self.communication = threading.Thread(target=self.communication_loop, name='communication_loop')
        self.connection = threading.Thread(target=self.connection_loop, name='connection_loop')

    def start_communication(self):
        self.run = True
        self.com_standby = True
        self.communication.start()

    def start_connection(self):
        self.run = True
        self.con_standby = True
        self.connection.start()

    def resume_communication(self):
        self.run = True
        self.com_standby = False

    def resume_connection(self):
        self.run = True
        self.con_standby = False

    def pause_communication(self):
        self.run = True
        self.com_standby = True

    def pause_connection(self):
        self.run = True
        self.con_standby = True

    def end(self):
        self.run = False
        self.con_standby = False
        self.com_standby = False
        self.communication.join()
        self.connection.join()

    def get_messages(self):
        return self.messages

    def set_messages(self):
        return self.messages.clear()

    def set_ip_port(self, ip, port):
        self.input_ip = ip
        self.input_port = port

    def communication_loop(self):
        while self.run:
            while self.com_standby:
                time.sleep(1)
            try:
                op = self.client.recv(BUFFER_SIZE)
            except AttributeError:
                return 1
            if op == bytes('0', 'utf-8'):
                self.client.send_string(op, raw=True)
            elif op == bytes('zip', 'utf-8'):
                self.messages.append('FILE: Receiving ZIP')
                self.sig.emit()

                ZIP_NAME = 'target.zip'

                temp = os.path.join(self.SAVE_LOCATION, ZIP_NAME)
                fp = open(temp, 'wb')
                self.client.save_file(BUFFER_SIZE, fp)

                self.messages.append('FILE: Finished transfer zip')
                self.sig.emit()
                fp.close()

            elif op == bytes('image', 'utf-8'):
                fp = open('../save/shipment.jpg', 'wb')
                self.client.save_file(BUFFER_SIZE, fp)

            else:
                print('Connection Lost')
                self.messages.append('Error: Lost connection to server')
                self.messages.append('RESET')
                self.sig.emit()
                self.pause_communication()

            self.sig.emit()
            time.sleep(0.5)

    def connection_loop(self):
        while self.run:
            while self.con_standby:
                time.sleep(1)
            try:
                if self.client.set_client_connection(self.input_ip, self.input_port, self.reconnect_time) == 1:
                    self.messages.append(time_stamp(
                        dates=False) + 'Failed to start client')
                    self.sig.emit()
                    return 1
                else:
                    self.client.send_string(
                        self.client.get_client_name() + "///is online")
                    self.client.confirm_connection()

                    self.messages.append('BUTTON Connected')
                    self.messages.append(time_stamp(
                        dates=False) + 'Connected to server')

                    self.start_communication()
                    self.resume_communication()
                    self.sig.emit()
            except AttributeError:
                return 1  # Force thread to end
