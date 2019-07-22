import threading
from PyQt5 import QtCore
import time


class GenericThread(QtCore.QObject):
    # Kwars not supported yet
    def __init__(self, server, callback, args=None, refresh_rate=0.5, sleep=1):
        # Initialize the parent class
        super(GenericThread, self).__init__()

        # Initializing the variables
        self.sig = QtCore.pyqtSignal()
        self.run = False
        self.standby = True
        self.server = server
        self.callback = callback
        self.refresh_rate = refresh_rate
        self.sleep = sleep

        # Initializing thread
        self.args = tuple()
        if args is not None:
            for arg in args:
                self.args += arg,

        self.main_thread = threading.Thread(target=self.main_loop, args=self.args)

    def main_loop(self, *argv):
        while self.run:
            while self.standby:
                time.sleep(self.sleep)
            if self.run and not self.standby:
                break
            self.callback(*argv)
            self.sig.emit()
            time.sleep(self.refresh_rate)
        return 0

    # Starting Thread, puts thread on standby
    def start(self):
        self.pause()
        try:
            self.main_thread.start()
        except RuntimeError:
            return 1
        return 0

    # Resumes the thread from standby
    def resume(self):
        self.run = True
        self.standby = False

    # Pauses the thread and puts it on standby
    def pause(self):
        self.run = True
        self.standby = True
        return 0

    # Ends the thread completely
    def end(self):
        # Close server before calling else the program might hang
        self.run = False
        self.standby = False
        self.main_thread.join()
        return 0
