# Tzu-Chi (Jerry), Kuo 2019
# jerrykuo820@gmail.com
# www.jerry-kuo.com
#
# Designed for Antiloop Studio. July 2019
# ========================================

import datetime
import os

from watchdog.observers import Observer as Obs
from PyQt5 import QtCore

from .server import Server
from .utils import zip_folder, print_error, time_stamp
from .error import Error as er
from .logger import _ObserverLog

# TODO(Jerry): July 25, 2019
#  Impletment time changes

print_to = None

class Observer(QtCore.QObject):
    """ Instance that watches the changes of a directory

    Working on two different modes. Timed based or change based.

    Attributes:
        obs: the watchdog instance. Read watchdog documentation for more info
        server: the server to report the changes to
        messages: for triggering the QtSignal and print the messages to GUI
        lib_path: default base path
        target_path: rest of the path (from lib_path) to the target directory.
                     For the ease of naming zip file.
        tot_path: lib_path + target_path
        handler: class that handles the directory changes accordingly
        mode: 0 for change based mode
              1 for time based mode
    """
    sig = QtCore.pyqtSignal()

    def __init__(self, server: Server, lib_path: str, target_path: str):
        super(Observer, self).__init__()

        self.obs = Obs()
        self.server = server
        self.messages = []
        self.log = _ObserverLog()

        self.lib_path = lib_path
        self.target_path = target_path
        self.tot_path = os.path.join(lib_path, target_path)
        self.mode = 0

    def dispatch(self, event):
        """ dispatch the calling cases to other methods

        MUST NOT CHANGE METHOD NAME. Else, it will not work.

        :param event: the triggering signals
        :return: returns 1 if no according changes known
                 returns 0 if no error
        """
        # TODO(Jerry): July 22, 2019
        #  remove the print statements and somehow append to log box
        if event.src_path.endswith('.log'):
            self.messages.append(time_stamp(dates=False) + 'Logfile modified')
            self.sig.emit()

            filename = os.path.join(
                '../archive', str(datetime.date.today()))

            self.messages.append(time_stamp(dates=False) + 'Output: ' + filename)
            self.messages.append(time_stamp(dates=False) + 'Target: ' + self.tot_path)
            self.sig.emit()
            
            if zip_folder( self.tot_path, filename):
                self.messages.append(time_stamp(_type=2, dates=False)
                                      + 'Error: ZIP failed')
                return er.Other

            self.messages.append(time_stamp(dates=False) +'Target Zipped')
            self.sig.emit()

            retval = self.server.broadcast_string('zip')
            print_error(retval, 'observer.Hanlder.dispatch:: Sending zip', print_to)

            retval = self.server.broadcast_zip(filename + '.zip')
            print_error(retval, 'Zip Sent', print_to)

            self.messages.append(time_stamp(dates=False) +'File Sent')
            self.sig.emit()
        else:
            return er.NoSuchOp
        return 0

    def set_server(self, server: Server) -> int:
        """ Sets the server of the observer

        :param server: the new server binded to the observer
        :return: returns 0 if no error
        """
        self.server = server
        return 0

    def get_target_path(self) -> str:
        """ Gets the target_path of the observer

        :return: returns the target path
        """
        return self.target_path

    def get_mode(self) -> int:
        """ Gets the mode the observer

        :return: returns the mode
        """
        return self.mode

    def get_messages(self):
        return self.messages

    def set_messages(self):
        return self.messages.clear()

    def set_mode(self, mode: int):
        """ Sets the mode of the observer

        :param mode: 0 for change based
                     1 for time based
                     else false
        :return: returns 1 for unknown mode
                 returns 0 if no error
        """
        if mode != 0 and mode != 1:
            return 1
        self.mode = mode
        return 0

    def start_observe(self, recursive: bool = False) -> int:
        """ Initializes the observer and gets it to start observing

        :param recursive: if the observer observes the nested folders
        :return: returns 1 if observer fails to initialize
                 returns 0 if no error
        """
        try:
            self.obs.schedule(self, self.tot_path, recursive)
            self.obs.start()
        except RuntimeError:
            return 1
        return 0


        """ Resumes the observer

        :return: returns 0 if no error
        """
        self.handler.pause = False
        return 0

    def close(self) -> int:
        """ Closes the observer thread

        :return: returns 1 if observer fails to close
                 returns 0 if no error
        """
        try:
            self.obs.stop()
            self.obs.join()
        except RuntimeError:
            return 1
        return 0

    def get_details(self):
        """ Get the details of the handler

        :return: returns all the details in a list
        """
        return self.log.get_latest_log()
