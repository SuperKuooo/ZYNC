# Tzu-Chi (Jerry), Kuo 2019
# jerrykuo820@gmail.com
# www.jerry-kuo.com
#
# Designed for Antiloop Studio. July 2019
# ========================================

import shutil
import datetime
import socket

from typing import List
from struct import pack, unpack
from .error import Error

# TODO(Jerry): July 23, 2019
# Look into problem with relative import and stuff

FAST_RECEIVE = 4194304
SLOW_RECEIVE = 4096


def zip_folder(target: str, output: str) -> int:
    """ Zips the target directory and saves it to output directory

    :param output: Where the zipped directory is saved
    :param target: The target directory(Directory being zipped)
    :return: Return 1 if zip error. Else return 0
    """
    try:
        shutil.make_archive(output, "zip", target)
    except shutil.Error:
        return 1
    return 0


def unzip_folder(target: str, output=None) -> int:
    """ Zips the target directory and saves it to output directory

    :param output: Where the zipped directory is saved
    :param target: The target directory(Directory being zipped)
    :return: Return 1 if zip error. Else return 0
    """
    try:
        if output is not None:
            shutil.unpack_archive(target, extract_dir=output)
        else:
            shutil.unpack_archive(target)
    except shutil.Error:
        return 1
    return 0


def check_connection(list_of_connection: List[socket.socket]) -> List[socket.socket]:
    """ Checks if the passed in list of client connections are still alive

    :param list_of_connection: List of client connection
    :return: return the dead clients that were popped of the list
    """

    _list = []
    i = 0
    for _socket in list_of_connection:
        b = pack('>I', 1) + b'0'
        try:
            _socket.send(b)
        except socket.error:
            _list.append(list_of_connection[i])
            list_of_connection.pop(i)
        i += 1
    return _list


def print_error(retval, message=None, print_to=None):
    if print_to == 'console':
        print(print_to)
        if retval == Error.NoFile:
            print('Error: Failed to open file')
        elif retval == Error.NoRecvTarget:
            print('Error: Empty Target')
        elif retval == Error.FailToSend:
            print('Error: Failed To send')
        elif retval == Error.FailToInitialize:
            print('Error: Failed To Initialize')
        elif retval == Error.FailSocketOp:
            print('Error: Socket operation failed')
        elif retval == Error.NoSuchOp:
            print('Error: Invalid input operation')
        elif retval == Error.CloseSocket:
            print('Error: Closing socket')
        elif message:
            print(message)
    elif print_to is list:
        if retval == Error.NoFile:
            print_to.append('Error: Failed to open file')
        elif retval == Error.NoRecvTarget:
            print_to.append('Error: Empty Target')
        elif retval == Error.FailToSend:
            print_to.append('Error: Failed To send')
        elif retval == Error.FailToInitialize:
            print_to.append('Error: Failed To Initialize')
        elif retval == Error.FailSocketOp:
            print_to.append('Error: Socket operation failed')
        elif retval == Error.NoSuchOp:
            print_to.append('Error: Invalid input operation')
        elif retval == Error.CloseSocket:
            print_to.append('Error: Closing socket')
        elif message:
            print_to.append(message)

def time_stamp(
        _type: int = 0, dates: bool = True, microsecond: bool = True
) -> str:
    # TODO(Jerry): July 25, 2019
    #   Clean up the code. Better interface
    """ Creates time stamps

    1: conn
    2: Error
    3: file name
    else: Debug

    :param _type: specifies the type of time stamp needed
    :param dates: If date is included in time stamp
    :param microsecond: if microsecond is included in time stamp
    :return: returns the created time stamp
    """
    if dates:
        stamp = datetime.datetime.now()
    else:
        stamp = datetime.datetime.now().time()
    
    if not microsecond:
        stamp = stamp.replace(microsecond=0)

    if _type == 1:
        temp = 'Conn: '
    elif _type == 2:
        temp = 'Error: '
    elif _type == 3:
        return str(datetime.date.today())
    elif _type == 4:
        temp = ''
    else:
        temp = 'Debug: '

    return str(stamp) + " " + temp


class Configuration:
    default_file = None

    def __init__(self):
        pass

    def set_config_file(self):
        try:
            f_pointer = open('./config.txt', 'r', encoding='utf-8')
        except FileNotFoundError:
            return 1

        for line in f_pointer:
            line = line.rstrip("\n").split(";")

            print(line)

        return 0


if __name__ == '__main__':
    cf = Configuration()
    cf.set_config_file()
