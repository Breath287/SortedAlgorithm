from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import json
import time



class Filehandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        for filename in os.listdir(track_folder):
            src = track_folder + "/" + filename
            new_destination = folder_destination + "/" + filename
            os.rename(src, new_destination)


track_folder = '/Users/jieli/Desktop/track_folder'
folder_destination = '/Users/jieli/Desktop/download_file'
event_handler = Filehandler()
observer = Observer()
observer.schedule(event_handler, track_folder, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()

