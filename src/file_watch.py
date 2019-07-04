import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, PatternMatchingEventHandler
import handler


class MyHandler(PatternMatchingEventHandler):
    def process(self, event):
        print("I am being processed")
        LoggingEventHandler()

    def on_modified(self, event):
        print("mod")
        self.process(event)

    def on_created(self, event):
        print("create")
        self.process(event)

    def on_moved(self, event):
        print("move")
        self.process(event)

    def on_deleted(self, event):
        print("del")
        self.process(event)


if __name__ == "__main__":
    logging.basicConfig(filename="./log/watch.log",
                        level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

path = "C:/Users/user/Documents/Unity_Build_Library/Univrse-Core"
observer = Observer()
observer.schedule(MyHandler(), path, recursive=True)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
