from PyQt5 import QtCore
import threading
import os
from socket_wrapper.Utils import *

BUFFER_SIZE = 4096
input_ip = None
input_port = None
reconnect_time = 3


class ClientConnectionThread(QtCore.QObject):
    sig = QtCore.pyqtSignal()
    messages = []
    SAVE_LOCATION = '..\\..\\save'
    RUN = False
    com_standby = True
    con_standby = True

    def init(self):
        self.communication_loop = threading.Thread(target=self.communication_loop, name='communication_loop')
        self.connection_loop = threading.Thread(target=self.connection_loop, name='connection_loop')

        self.pause_communication()
        self.pause_connection()

        self.communication_loop.start()
        self.connection_loop.start()

    def start_communication(self):
        self.RUN = True
        self.com_standby = False

    def start_connection(self):
        self.RUN = True
        self.con_standby = False

    def pause_communication(self):
        self.RUN = True
        self.com_standby = True

    def pause_connection(self):
        self.RUN = True
        self.con_standby = True

    def end(self):
        self.RUN = False
        self.con_standby = False
        self.com_standby = False
        self.communication_loop.join()
        self.connection_loop.join()

    def get_messages(self):
        return self.messages

    def set_messages(self):
        return self.messages.clear()

    def communication_loop(self):
        global client
        while self.RUN:
            while self.com_standby:
                time.sleep(1)
            try:
                op = client.recv(BUFFER_SIZE)
            except AttributeError:
                return 1
            if op == bytes('0', 'utf-8'):
                client.send_string(op, raw=True)
            elif op == bytes('zip', 'utf-8'):
                self.messages.append('FILE: Receiving ZIP')
                self.sig.emit()

                ZIP_NAME = 'target.zip'

                temp = os.path.join(self.SAVE_LOCATION, ZIP_NAME)
                fp = open(temp, 'wb')
                client.save_file(BUFFER_SIZE, fp)

                self.messages.append('FILE: Finished transfer zip')
                self.sig.emit()
                fp.close()

            elif op == bytes('image', 'utf-8'):
                fp = open('../save/shipment.jpg', 'wb')
                client.save_file(BUFFER_SIZE, fp)

            else:
                print('Connection Lost')
                self.messages.append('Error: Lost connection to server')
                self.messages.append('RESET')
                self.sig.emit()
                self.pause_communication()

            self.sig.emit()
            time.sleep(0.5)

    def connection_loop(self):
        while self.RUN:
            while self.con_standby:
                time.sleep(1)
            try:
                if client.set_client_connection(input_ip, input_port, reconnect_time) == 1:
                    self.messages.append(time_stamp(
                        dates=False) + 'Failed to start client')
                    self.sig.emit()
                    return 1
                else:
                    client.send_string(
                        client.get_client_name() + "///is online")
                    client.confirm_connection()

                    self.messages.append('BUTTON Connected')
                    self.messages.append(time_stamp(
                        dates=False) + 'Connected to server')

                    self.start_communication()
                    self.pause_connection()
                    self.sig.emit()
            except AttributeError:
                return 1  # Force thread to end
