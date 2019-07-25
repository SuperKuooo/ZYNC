# Tzu-Chi (Jerry), Kuo 2019
# jerrykuo820@gmail.com
# www.jerry-kuo.com
#
# Designed for Antiloop Studio. July 2019
# ========================================

import socket
import time
import struct
from .error import Error as er


class Client:
    """ Creates a client connection that receives from server

    A mid-level wrapper based on socket module.
    Takes care of reconnection, keeping client connection alive,
    receiving the zips, and etc

    Attributes:
        name: Local client name
        s: low-level socket that is being wrapped by.

    """

    def __init__(self, conn: socket.socket = None):
        self.name = socket.gethostname()
        self.s = conn

    def set_client_connection(self,
                              input_ip: str,
                              input_port: int,
                            ) -> int:
        """ Connects the client socket to specific address and port

        :param input_ip: the target ip
        :param input_port: the target port
        :param time_to_reconnect: interval for reconnecting
        :param num_of_reconnects: number of tries to reconnect
        :return: returns 1 if ran out of tries to reconnect
                 returns 0 if no error
        """
        # TODO(Jerry): July 22, 2019
        #  Change where reconnecting statement is printing
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.settimeout(2)
            self.s.connect((input_ip, input_port))
        except socket.error:
            return er.FailSocketOp
        return 0

    def get_client_name(self) -> str:
        """ Gets the name of the client

        :return: the name of the client
        """
        return self.name

    def confirm_connection(self, message=None):
        """ Sends a message to confirm the connection with the server

        :param message: the outgoing echo message
        :return raises user warning if outgoing and incoming messages are different
                returns 0 if no error

        """
        if not message:
            # Sets default message if not specified
            message = self.name + '///is online'

        self.s.settimeout(5)
        data = self.recv().decode('utf-8')

        if data != message:
            # Compares the outgoing and incoming messages
            print('Outgoing:', message)  # Outgoing
            print('Incoming: ', data)    # Incoming
            raise UserWarning('Error: Different echo value')
        return 0

    def recv(self, timeout: int = 5):
        """ Receives from the server

        Source:: https://stackoverflow.com/questions/17667903/python-socket-receive-large-amount-of-data

        :param buffer_size: the size to receive at once
        :param timeout: timeout time
        :return: returns 1 if socket timed out and doesn't receive anything
                 returns whatever is receive from the socket
        """
        self.s.settimeout(timeout)

        try:
            raw_msglen = self.s.recv(4)
        except socket.error:
            return er.FailSocketOp
        if not raw_msglen:
            return er.Other
        msglen = struct.unpack('>I', raw_msglen)[0]

        data = b''
        while len(data) < msglen:
            try:
                packet = self.s.recv(msglen-len(data))
            except socket.error:
                return er.FailSocketOp
            if not packet:
                return None
            data += packet
        return data

    def send_string(self, message, raw: bool = False) -> int:
        """ sends a string from client to server

        :param message: the string that is going to the server
        :param raw: if the message has been decoded or not
        :return: returns 1 if it fails to send message
                 returns 0 if no error
        """
        # Encrypt message
        b = message
        if not raw:
            b = message.encode('utf-8')

        # Pack message with prefix
        b = struct.pack('>I', len(b)) + b
        try:
            self.s.send(b)
        except socket.error:
            # TODO(Jerry): July 22, 2019
            #  Remove the print statement and double checks
            #  everywhere else has error statement to catch
            #  the return value
            return er.FailToSend
        return 0

    def send_image(self, location: str) -> int:
        """ Sends images to server
        Note: Obsolete. Haven't tested for a while.
            Function may not work.

        :param location: directory of the outgoing image
        :return: returns 1 if the image fails to send
                 returns 0 if no error
        """
        try:
            with open(location, 'rb') as fp:
                b = bytearray(fp.read())
                self.s.sendall(b)
        except socket.error:
            print("Error: Failed to send image")
            return 1
        return 0

    def send_zip(self, location: str):
        """ Sends a zip from client to server

        :param location: directory of the outgoing zip file
        :return: returns 1 if the zip fails to send
                 returns 0 if no error
        """
        # >I might not be big enough to handle some of the files
        # Use Q. Look at struct documentation online
        try:
            with open(location, 'rb') as fp:
                stct_file = fp.read()
                stct_file = struct.pack('>I', len(stct_file)) + stct_file
                self.s.sendall(stct_file)
        except socket.error:
            return er.FailToSend
        return 0

    def save_file(self, buffer_size, file_pointer) -> int:
        """ saves the receiving data to the specified file pointer

        Since .recv() only receives N bytes at a time, so the best
         way is to repeatedly receive data and save it until there
        is nothing to receive.

        :param buffer: the buffer size for each receive
        :param file_pointer: where to save the incoming data
        :return: returns 1
        """
        data = self.recv()
        # This is temporary fix. Will come back to this after we have
        # multiple channels
        if data == b'0':
            self.save_file(buffer_size, file_pointer)
        
        for _ in range(0, len(data)//buffer_size):
            file_pointer.write(data[0:buffer_size])
            data = data[buffer_size:]
        file_pointer.write(data)
        return 0

    def close(self) -> int:
        """ Closes the client socket

        :return: return 0 if no error
        """
        self.s.close()
        return 0
