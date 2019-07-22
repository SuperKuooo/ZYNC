# Tzu-Chi (Jerry), Kuo 2019
# jerrykuo820@gmail.com
# www.jerry-kuo.com
#
# Designed for Antiloop Studio. July 2019
# ========================================

import datetime
import time
import os

from watchdog.observers import Observer as Obs
from .server import *

# TODO(Jerry): July 22, 2019
#  Re-examine the observer/handler structure
#  Need it for time changes
class Observer:
    """ Instance that watches the changes of a directory

    Working on two different modes. Timed based or change based.

    Attributes:
        obs: the watchdog instance. Read watchdog documentation for more info
        server: the server to report the changes to
        lib_path: default base path
        target_path: rest of the path (from lib_path) to the target directory.
                     For the ease of naming zip file.
        tot_path: lib_path + target_path
        handler: class that handles the directory changes accordingly
        mode: 0 for change based mode
              1 for time based mode
    """
    def __init__(self, server: Server, lib_path: str, target_path: str):
        self.obs = Obs()
        self.server = server
        self.lib_path = lib_path
        self.target_path = target_path
        self.tot_path = os.path.join(lib_path, target_path)
        self.handler = Handler(server, lib_path, target_path)
        self.mode = 0

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
            self.obs.schedule(self.handler, self.tot_path, recursive)
            self.obs.start()
        except RuntimeError:
            return 1
        return 0

    def pause_observe(self):
        """ Pauses the observing

        :return: returns 0 if no error
        """
        self.handler.pause = True
        return 0

    def resume_observe(self):
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


class Handler:
    """ Acts accordingly when file changes

    Attributes:
        server: the server that is distributing the files
        lib_path: same as observer
        target_path: same as observer
        tot_path: same as observer
        last_success: time of last success send
        last_attempt: time of last attempt
        total_attempts: number of total attempts
        save_directory: the directory files are being saved at
        pause: if observing should be stopped
    """
    def __init__(self, server: Server, lib_path: str, target_path: str):
        self.server = server
        self.lib_path = lib_path
        self.target_path = target_path
        self.tot_path = os.path.join(lib_path, target_path)

        self.last_success = None
        self.last_attempt = None
        self.total_attempts = None
        self.save_directory = None

        self.pause = False

    def dispatch(self, event):
        """ dispatch the calling cases to other methods

        MUST NOT CHANGE METHOD NAME. Else, it will not work.

        :param event: the triggering signals
        :return: returns 1 if no according changes known
                 returns 0 if no error
        """
        # TODO(Jerry): July 22, 2019
        #  remove the print statements and somehow append to log box
        if not self.pause:
            if event.src_path.endswith('.log'):
                print('Logfile Modified')
                filename = os.path.join('./archive', self.target_path, str(datetime.date.today()))
                
                if zip_folder(filename, self.tot_path):
                    print('Error: ZIP failed')
                print('zipped')

                self.server.broadcast_string('zip')
                time.sleep(0.5)
                print('sending zip')
                self.server.broadcast_zip(os.path.join(
                    './archive', self.target_path, str(datetime.date.today()) + '.zip'))
                print('done shipping')
            else:
                return 1
        return 0

    def get_details(self):
        """ Get the details of the handler

        :return: returns all the details in a list
        """
        return [self.last_success, self.last_attempt, self.total_attempts, self.save_directory]
