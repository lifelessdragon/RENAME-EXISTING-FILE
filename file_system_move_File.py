import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return
        elif event.event_type == 'created':
            print(f'File {event.src_path} has been created.')

        elif event.event_type == 'deleted':
            print(f'File {event.src_path} has been deleted.')

        elif event.event_type == 'modified':
            print(f'File {event.src_path} has been modified.')

            source = 'main.txt'
            dest = 'newfile.txt'

            try:
                os.rename(source, dest)
                print(f'Renamed {source} to {dest}')
            except FileNotFoundError:
                print(f'Error: {source} not found.')

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='Project115', recursive=False)

    print("Watching for file system events. Press Ctrl+C to stop.")
    observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()

    observer.join()