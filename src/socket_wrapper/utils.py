# Tzu-Chi (Jerry), Kuo 2019
# jerrykuo820@gmail.com
# www.jerry-kuo.com
#
# Designed for Antiloop Studio. July 2019
# ========================================

import shutil

from typing import List

from .client import *

import datetime


def zip_folder(output: str, target: str) -> int:
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


def check_connection(list_of_connection: List[socket.socket]) -> List[socket.socket]:
    """ Checks if the passed in list of client connections are still alive

    :param list_of_connection: List of client connection
    :return: return the dead clients that were popped of the list
    """
    _list = []
    i = 0

    for _socket in list_of_connection:
        temp = Client(_socket)
        if temp.send_string('0'):
            _list.append(list_of_connection[i])
            list_of_connection.pop(i)
        elif temp.recv(1) == 1:
            _list.append(list_of_connection[i])
            list_of_connection.pop(i)
        i += 1
    return _list


def time_stamp(
        _type: int = 0, dates: bool = True, microsecond: bool = True
) -> str:
    """ Creates time stamps

    :param _type: specifies the type of time stamp needed
    :param dates: If date is included in time stamp
    :param microsecond: if microsecond is included in time stamp
    :return: returns the created time stamp
    """
    if dates:
        stamp = datetime.datetime.now
    else:
        stamp = datetime.datetime.now().time()

    if _type == 1:
        temp = 'Conn: '
    elif _type == 2:
        temp = 'Error: '
    elif _type == 3:
        temp = 'project'
    else:
        temp = 'Debug: '

    if not microsecond:
        stamp = stamp.replace(microsecond=0)

    return str(stamp) + " " + temp