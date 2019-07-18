from watchdog.observers import Observer as Obs
from .Server import *
import os


class Observer:
    def __init__(self, server: Server, lib_path: str, target_path: str):
        self.obs = Obs()
        self.server = server
        self.lib_path = lib_path
        self.target_path = target_path
        self.tot_path = os.path.join(lib_path, target_path)
        self.handler = Handler(server, lib_path, target_path)
        # TODO: add a timing mode
        # self.mode = True

    def set_server(self, server: Server):
        self.server = server
        return 0

    def get_target_path(self) -> str:
        return self.target_path

    def start_observe(self, recursive: bool = False) -> int:
        try:
            self.obs.schedule(self.handler, self.tot_path, recursive)
            self.obs.start()
        except RuntimeError:
            return 1
        return 0

    def close(self) -> int:
        try:
            self.obs.stop()
            self.obs.join()
        except RuntimeError:
            return 1
        return 0


class Handler:
    def __init__(self, server: Server, lib_path: str, target_path: str):
        self.server = server
        self.lib_path = lib_path
        self.target_path = target_path
        self.tot_path = os.path.join(lib_path, target_path)
        self.last_success = 'tdoay'
        self.last_attempt = '56 mins ago'
        self.total_attempts = 16
        self.save_directory = '/usr'

    def dispatch(self, event):
        if event.src_path.endswith('.log'):
            print('Logfile Modified')
            filename = os.path.join('./archive', self.target_path, str(DATE))
            if zip_folder(filename, self.tot_path):
                print('Error: ZIP failed')
            else:
                print('zipped')

            self.server.broadcast_string('zip')
            time.sleep(0.5)
            print('sending zip')
            self.server.broadcast_zip(os.path.join(
                './archive', self.target_path, str(DATE) + '.zip'))
            print('done shipping')
        else:
            return 1
        return 0

    def get_details(self):
        return [self.last_success, self.last_attempt, self.total_attempts, self.save_directory]
