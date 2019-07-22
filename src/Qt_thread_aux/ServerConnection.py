import threading
from PyQt5 import QtCore
from socket_wrapper.utils import *


class ServerConnectionThread(QtCore.QObject):
    sig = QtCore.pyqtSignal()

    def __init__(self, server, refresh_rate=0.5, sleep=1, max_connection=5, buffer_size=4096):
        # Initializing variables
        super(ServerConnectionThread, self).__init__()
        self.run = False
        self.standby = True
        self.server = server
        self.refresh_rate = refresh_rate
        self.sleep = sleep
        self.max_connection = max_connection
        self.buffer_size = buffer_size

        # Initializing threads
        self.connection = threading.Thread(target=self.connection_loop, name='connection_loop')
        self.alive_message = threading.Thread(target=self.alive_message_loop, name='alive_message_loop')

    def start(self):
        self.pause()
        try:
            self.connection.start()
            self.alive_message.start()
        except RuntimeError:
            return 1
        return 0

    def resume(self):
        self.run = True
        self.standby = False
        return 0

    def pause(self):
        self.run = True
        self.standby = True
        return 0

    def end(self):
        self.run = False
        self.standby = False
        self.connection.join()
        self.alive_message.join()
        return 0

    def set_sig(self, func):
        self.sig.connect(func)

    def connection_loop(self):
        while self.run:
            while self.standby:
                time.sleep(self.sleep)
            if self.run and not self.standby:
                self.server.listen(self.max_connection)
                conn, addr = self.server.accept()
                self.server.echo_connection(conn, conn.recv(self.buffer_size))
                self.sig.emit()
        return 0

    def alive_message_loop(self):
        while self.run:
            while self.standby:
                time.sleep(self.sleep)
            if self.run and not self.standby:
                if not self.server.get_list_of_connection():
                    continue
                if check_connection(self.server.get_list_of_connection()):
                    self.sig.emit()
            time.sleep(self.refresh_rate)
        return 0
