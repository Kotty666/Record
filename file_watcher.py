#!/usr/bin/python3
# require sudo sysctl fs.inotify.max_user_watches=100000
import time
from PLOG import logger
from converter import Convert
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

class Watcher:
    def __init__(self,path) -> None:
        patterns = ["*"]
        ignore_patterns = None
        ignore_directories = False
        case_sensitive = True
        my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
        my_event_handler.on_created = self.on_created
        go_recursively = False
        my_observer = Observer()
        my_observer.schedule(my_event_handler, path, recursive=go_recursively)

        my_observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            my_observer.stop()
            my_observer.join()
            pass

    def on_created(self,event):
        logger(f"The file {event.src_path} has been created. Calling Converter")
        Convert(event.src_path)

if __name__ == "__main__":
    Watcher('/home/kotty/test')