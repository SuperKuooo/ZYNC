import threading
import os
import time

from PyQt5 import QtCore
from socket_wrapper.utils import time_stamp, print_error, FAST_RECEIVE, unzip_folder
from socket_wrapper.error import Error as er


# TODO(Jerry): July 25th, 2019
#   Replace this with generic thread
#   Much more efficient
print_to = None
save_dir = 'C:/Users/user/Desktop/ZYNC/save/Unpacked/'


class ClientConnectionThread(QtCore.QObject):
    sig = QtCore.pyqtSignal()

    def __init__(self, client, input_ip=None, input_port=None):
        # Initializing Vairables
        super(ClientConnectionThread, self).__init__()
        self.client = client
        self.messages = []
        self.SAVE_LOCATION = '..\save'
        self.run = False
        self.com_standby = True
        self.con_standby = True
        self.input_ip = input_ip
        self.input_port = input_port

        # Initializing threads
        self.communication = threading.Thread(
            target=self.communication_loop, name='communication_loop')
        self.connection = threading.Thread(
            target=self.connection_loop, name='connection_loop')

    def start_communication(self):
        self.run = True
        self.com_standby = True
        if not self.communication.isAlive():
            self.communication.start()

    def start_connection(self):
        self.run = True
        self.con_standby = True
        if not self.connection.isAlive():
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
        try:
            self.communication.join()
            self.connection.join()
        except RuntimeError:
            return 1
        return 0

    def get_messages(self):
        return self.messages

    def set_messages(self):
        return self.messages.clear()

    def set_ip_port(self, ip, port):
        self.input_ip = ip
        self.input_port = port

    def set_reconnect_time(self, _time):
        self.reconnect_time = _time

    def set_buffer_size(self, size):
        self.buffer_size = size

    def communication_loop(self):
        while self.run:
            while self.com_standby:
                time.sleep(1)

            # TODO(Jerry): July 22, 2019
            #  Bug: After receiving zip, client disconnects without reason
            #       but is able to reconnect on its own.
            #  Reason: client cannot respond to check_connection while
            #          receiving zip

            try:
                op = self.client.recv()
            except AttributeError:
                return er.CloseSocket

            if op == b'zip':
                self.messages.append(time_stamp(dates=False) + 'Receiving ZIP')
                self.sig.emit()

                i = 0
                retval = 1
                while retval != 0:
                    ZIP_NAME = time_stamp(3) + '-{}.zip'.format(i)
                    print(ZIP_NAME)
                    path = os.path.join(self.SAVE_LOCATION, ZIP_NAME)
                    retval = self.client.save_file(FAST_RECEIVE, path)
                    if  retval == er.NoFile:
                        i += 1
                    
                self.messages.append(time_stamp(dates=False) + 'ZIP Received')
                self.messages.append('FILE ' + path)
                self.sig.emit()
                temp_dir = save_dir + time_stamp(3)+'-{}'.format(i)
                os.mkdir(temp_dir)
                unzip_folder(os.path.join(self.SAVE_LOCATION, ZIP_NAME), temp_dir)
                

            elif op == bytes('image', 'utf-8'):
                fp = open('../save/shipment.jpg', 'wb')
                self.client.save_file(self.buffer_size, fp)

            elif op != b'0':
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
                reconn_time = 3
                while self.client.set_client_connection(self.input_ip, self.input_port):
                    self.messages.append(time_stamp(
                        1, False) + 'Failed to conned')
                    self.messages.append(time_stamp(
                        1, False) + 'Reconnecting in {} seconds'.format(reconn_time))
                    self.sig.emit()
                    time.sleep(reconn_time)

                self.client.send_string(
                    self.client.get_client_name() + "///is online")
                self.client.confirm_connection()

                self.messages.append('BUTTON CONNECTED')
                self.messages.append(time_stamp(
                    dates=False) + 'Connected to server')

                self.start_communication()
                self.resume_communication()
                self.pause_connection()
                self.sig.emit()
            except AttributeError:
                return 1  # Force thread to end
