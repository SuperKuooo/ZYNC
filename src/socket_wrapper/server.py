# Tzu-Chi (Jerry), Kuo 2019
# jerrykuo820@gmail.com
# www.jerry-kuo.com
#
# Designed for Antiloop Studio. July 2019
# ========================================

import socket
import time

from typing import List, Union, Tuple
from .client import Client
from .error import Error as er
from .utils import print_error

# TODO(Jerry): July 23, 2019
#  add channels to support
#  RIP. That's a ton of work to do it right.
#  Look into async and other stuff to make it work.

# TODO(Jerry): July 23, 2019
#   Change data packing style to packets


class Server:
    """ Creates a server wrapper that hosts connection and watches file changes

    Initializes a higher-level server instance for users to interact.
    Takes care of reconnection, echo connection, and etc.

    Attributes:
        list_of_connection: List of client connections to server
        list_of_observer: List of directories the server is watching for changes
        name: The computer name of the current server
        s: The level socket. Bind to specific address and acts as server
    """

    def __init__(self):
        self.list_of_connection = []
        self.list_of_observer = []
        self.name = socket.gethostname()
        self.s = None

    def set_server_connection(
            self, input_ip: str, input_port: int, attempt_to_reconnect: int = 0
    ) -> Union[int, Tuple[str, int]]:
        """ Bind server instance to specific ip. Retry if binding fails.

        :param input_ip: Target binding ip
        :param input_port: Target binding port
        :param attempt_to_reconnect: Wait time for reconnecting
        :return: returns 1 if cannot bind to ip
                 returns ip, port if socket binds successfully
        """
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.bind((input_ip, input_port))
        except socket.error:
            print("Error: Failed to start server")
            if attempt_to_reconnect:
                print("Retrying in " + str(attempt_to_reconnect) + " seconds...")
                time.sleep(attempt_to_reconnect)
                self.set_server_connection(
                    input_ip, input_port, attempt_to_reconnect)
            return er.FailSocketOp
        return input_ip, input_port

    def set_list_of_connection(
            self, _socket=None, operation: int = 0, index: int = None
    ) -> int:
        """ Edit the list of connected clients
        types of operation: Currently four types
            0: Append a socket to the list
            1: Set the current list to the new list
            2: Delete one item from the list by index
            3: Deletes the whole list

        :param _socket: Append this socket or set equal to the list
        :param operation: Type of operation (Specified above)
        :param index: The index of the deleting socket
        :return: returns 1 if failed to specify operation
                 returns 0 if operation executed successfully
        """
        if operation == 0:
            self.list_of_connection.append(_socket)
        elif operation == 1:
            self.list_of_connection = _socket
        elif operation == 2:
            if index is not None:
                self.list_of_connection.pop(index)
        elif operation == 3:
            self.list_of_connection.clear()
        else:
            return er.NoSuchOp
        return 0

    def set_list_of_observer(
            self, _observer=None, operation: int = 0, index: int = None
    ) -> int:
        """Edit the list of watching directories
        types of operation: Currently four types
            0: Append a observer to the list
            1: Set the current list to the new list
            2: Delete one item from the list by index
            3: Deletes the whole list

        :param _observer: Append this observer or set equal to the list
        :param operation: Type of operation (Specified above)
        :param index: The index of the deleting socket
        :return: returns 1 if failed to specify operation
                 returns 0 if operation executed successfully
        """
        if operation == 0:
            self.list_of_observer.append(_observer)
        elif operation == 1:
            self.list_of_observer = _observer
        elif operation == 2:
            if index is not None:
                self.list_of_observer[index].close()
                self.list_of_observer.pop(index)
        elif operation == 3:
            for obs in self.list_of_observer:
                obs.close()
            self.list_of_observer.clear()
        else:
            return er.NoSuchOp
        return 0

    def get_num_of_connection(self) -> int:
        """ Get the number of client connections

        :return: returns -1 if the list is None
                 returns list length
        """
        if self.list_of_connection is None:
            return er.EmptyResult
        else:
            return len(self.list_of_connection)

    def get_num_of_observer(self) -> int:
        """ Get the number of observers

        :return: returns -1 if the list is None
                 returns list length
        """
        if self.list_of_observer is None:
            return er.EmptyResult
        else:
            return len(self.list_of_observer)

    def get_list_of_connection(
            self, index: int = None) -> Union[List[socket.socket], socket.socket]:
        """ Get the list or specific connection details

        :param index: get the specific connection in the list
        :return: returns the whole list or the specific connection
        """
        if not index:
            return self.list_of_connection
        return self.list_of_connection[index]

    def get_list_of_observer(self, index: int = None):  # TODO(Jerry): Add type hint
        """ Get the list or specific observer details

        :param index: get the specific observer in the list
        :return: returns the whole list
                 returns the specific observer
        """
        if index is None:
            return self.list_of_observer
        return self.list_of_observer[index]

    def get_server_name(self) -> str:
        """ Get the server name

        :return: the server name
        """
        return self.name

    def echo_connection(self, conn: socket.socket, message):
        """ Echos connection to client when client first connects

        Double checks the connection with client
        If passes echo test, add client to connection list

        :param conn: The client connection
        :param message: Connection Message
        :return: returns 1 if failed to send message
                 returns 0 if no error
        """

        message = message.decode("utf-8")
        try:
            temp = Client(conn)
            temp.send_string(message)
            self.set_list_of_connection(conn)
        except socket.error:
            return er.FailToSend
        return 0

    def broadcast_string(self, message: str, client_index: int = None) -> int:
        """ Sends string to target client(s)

        :param message: The delivering message
        :param client_index: Specifies the target client by index
        :return: returns 1 if failed to send message
                 returns 0 if no error
        """
        if client_index is None:
            target_audience = self.get_list_of_connection()
        else:
            target_audience = self.get_list_of_connection(client_index)

        for conn in target_audience:
            try:
                temp = Client(conn)
                temp.send_string(message)
            except socket.error:
                return er.FailToSend
        return 0

    def broadcast_zip(self, location: str, client_index: int = None):
        """ Sends zip to target client(s)

        :param location: Location of outgoing zip
        :param client_index: Specifies the target client by index
        :return: returns 1 if failed to send zip
                 returns 0 if no error
        """

        #TODO (Jerry): July 24, 2019
        # Add a double check method that sends a string to check
        # if zip has actually been received

        if client_index is None:
            target_audience = self.get_list_of_connection()
        else:
            target_audience = self.get_list_of_connection(client_index)
        
        if not target_audience:
            return er.NoRecvTarget
        
        for conn in target_audience:
            try:
                temp = Client(conn)
                retval = temp.send_zip(location)
                print_error(retval, 'server.broadcast_zip:: Sent')
            except socket.error:
                return er.FailToSend
        return 0

    def close(self):
        """ Terminates the server

        :return: returns 0 if no error
        """
        for conn in self.list_of_connection:
            conn.close()
        for obs in self.list_of_observer:
            obs.close()
        if self.s is not None:
            self.s.close()
        return 0

    def listen(self, size: int):
        """ Listen for connection

        :param size: number of queue
        :return: whatever self.s.listen returns lol
        """
        try:
            return self.s.listen(size)
        except socket.error:
            # Catches error when terminating the server.
            return er.CloseSocket

    def accept(self):
        """ Accepts the connection

        :return: whatever self.s.accept returns lol
        """
        try:
            return self.s.accept()
        except socket.error:
            # Cathches error when terminating the server
            return er.CloseSocket, er.CloseSocket
