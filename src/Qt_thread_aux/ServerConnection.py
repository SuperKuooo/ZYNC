# Tzu-Chi (Jerry), Kuo 2019
# jerrykuo820@gmail.com
# www.jerry-kuo.com
#
# Designed for Antiloop Studio. July 2019
# ========================================

import threading
import time

from PyQt5 import QtCore
from socket_wrapper.utils import check_connection
from socket_wrapper.client import Client


class ServerConnectionThread(QtCore.QObject):
    """ Initializes a thread that updates the server/client connection    
    
    - Connection loop continously listens for new client connection
    - Alive message loop updates every N seconds and check if 
        any of the connected client has died

    Attributes:
        run: Terminates the loops
        standby: Pauses the check connection and listen loop
        server: The server that connects to the clients
        refresh_rate: Refresh rate for checking connection, in seconds
        sleep: Standby loop refresh rate, in seconds
        max_connection: Max number to listen for at a time
        buffer_size: Size of message to receive
    """
    sig = QtCore.pyqtSignal()

    def __init__(self, server):
        # Initializing variables
        super(ServerConnectionThread, self).__init__()
        self.run = False
        self.alive_standby = True
        self.conn_standby = True
        self.server = server
        self.refresh_rate = 0.5
        self.sleep = 1
        self.max_connection = 5
        self.buffer_size = 4096

        # Initializing threads
        self.connection = threading.Thread(target=self.connection_loop, name='connection_loop')
        self.alive_message = threading.Thread(target=self.alive_message_loop, name='alive_message_loop')

    def start(self):
        """ Set loop to pause state and initialize thread
        
        :return: returns 1 if attempt to start thread twice
                 returns 0 if no error
        """
        self.pause_conn()
        self.pause_alive()
        try:
            self.connection.start()
            self.alive_message.start()
        except RuntimeError:
            return 1
        return 0

    def resume_conn(self):
        """ Moves thread out of standby state
        
        :return: returns 0 if no error
        """
        self.run = True
        self.conn_standby = False
        return 0

    def resume_alive(self):
        """ Moves thread out of standby state
        
        :return: returns 0 if no error
        """
        self.run = True
        self.alive_standby = False
        return 0


    def pause_conn(self):
        """ Pauses the thread and it on stanby state
        
        :return: returns 0 if no error
        """
        self.run = True
        self.conn_standby = True
        return 0

    def pause_alive(self):
        """ Pauses the thread and it on stanby state
        
        :return: returns 0 if no error
        """
        self.run = True
        self.alive_standby = True
        return 0       

    def end(self):
        """ Breaks out of the loops and join the threads
        
        :return: returns 0 if no error
        """
        self.run = False
        self.conn_standby = False
        self.alive_standby = False
        self.connection.join()
        self.alive_message.join()
        return 0

    def set_sig(self, func):
        """ Bound the signal to the specified function
        
        :return: returns 0 if no error
        """
        self.sig.connect(func)
        return 0

    def connection_loop(self):
        """ Listen for new connections

        Triggers the callback (self.sig) when new connection has been made.
        
        :return: returns 0 if no error

        """
        while self.run:
            while self.conn_standby:
                time.sleep(self.sleep)
            if self.run and not self.conn_standby:
                self.server.listen(self.max_connection)
                conn, addr = self.server.accept()
                if conn == addr and conn == 1:
                    continue
                self.server.echo_connection(conn, Client(conn).recv())
                self.sig.emit()
        return 0

    def alive_message_loop(self):
        """ Checks if the connected clients are still alive.
        
        :return: returns 0 if no error
        """
        # TODO(Jerry): July 22, 2019
        # pause check when sending zip.
        # Update July 23: Bigger problem, packing data, setting flags?
        while self.run:
            while self.alive_standby:
                time.sleep(self.sleep)
            if self.run and not self.alive_standby:
                if not self.server.get_list_of_connection():
                    continue
                if check_connection(self.server.get_list_of_connection()):
                    self.sig.emit()
            time.sleep(self.refresh_rate)
        return 0
