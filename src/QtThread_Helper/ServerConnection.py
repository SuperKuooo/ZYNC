import threading
from PyQt5 import QtCore
from socket_wrapper.Utils import *

MAX_CONNECTION = 5
BUFFER_SIZE = 4096


class ServerConnectionThread(QtCore.QObject):
    sig = QtCore.pyqtSignal()
    RUN = False
    standby = True
    server = None

    def init(self, _server):
        self.connection_loop = threading.Thread(target=self.connection_loop, name='connection_loop')
        self.alive_message_loop = threading.Thread(target=self.alive_message_loop, name='alive_message_loop')
        self.RUN = True
        self.server = _server

        self.connection_loop.start()
        self.alive_message_loop.start()

    def start(self):
        self.RUN = True
        self.standby = False

    def pause(self):
        self.RUN = True
        self.standby = True

    def end(self):
        if self.server:
            self.server.close()
        self.RUN = False
        self.standby = False
        self.connection_loop.join()
        self.alive_message_loop.join()
        return 0

    def connection_loop(self):
        while self.RUN:
            while self.standby:
                time.sleep(1)
            try:
                self.server.listen(MAX_CONNECTION)
                conn, addr = self.server.accept()
            except OSError:
                return 1  # Terminating the server
            except AttributeError:
                return 1  # Forcing the program to end lmao

            self.server.echo_connection(conn, conn.recv(BUFFER_SIZE))
            self.sig.emit()
        return 0

    def alive_message_loop(self):
        while self.RUN:
            while self.standby:
                time.sleep(1)
            try:
                if not self.server.get_list_of_connection():
                    continue
                if check_connection(self.server.get_list_of_connection()):
                    self.sig.emit()
            except AttributeError:
                return 1  # Force Connection Close
            time.sleep(0.5)
        return 0
