from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from time import sleep
import logging

from os import scandir, makedirs
from os.path import exists, join, splitext
from shutil import move


source_dir = r"Enter Your Destination Folder"
dest_dir_audio = r"Enter Your Destination Folder\Audio"
dest_dir_video = r"Enter Your Destination Folder\Video"
dest_dir_image = r"Enter Your Destination Folder\Images"
dest_dir_docs = r"Enter Your Destination Folder\Documents"
dest_dir_apps = r"Enter Your Destination Folder\Applications"
dest_dir_zip =  r"Enter Your Destination Folder\Zip Files"


for folder in [dest_dir_audio, dest_dir_video, dest_dir_image, dest_dir_docs, dest_dir_zip, dest_dir_apps]:
    if not exists(folder):
        makedirs(folder)

image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".webp", ".tiff", ".bmp", ".svg", ".ico"]
video_extensions = [".mp4", ".mov", ".avi", ".flv", ".wmv", ".mkv", ".webm"]
audio_extensions = [".mp3", ".wav", ".aac", ".flac", ".wma", ".m4a"]
document_extensions = [".pdf", ".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx", "xlsm", "xlsb",".csv", ".odt"]
app_extensions = [".exe", ".msi", ".bat", ".cmd", ".com", ".jar", ".apk", ".app", ".bin", ".sh"]
archive_extensions = [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".iso", ".cab"]


def make_file_unique(dest_dir, name):
    filename, extension = splitext(name)
    counter = 1
    while exists(join(dest_dir, name)):
        name = f"{filename}({counter}){extension}"
        counter += 1
    return name

def move_files(dest_dir, entry, name):
    dest_path = join(dest_dir, name)
    if exists(dest_path):
        name = make_file_unique(dest_dir, name)
    move(entry.path, join(dest_dir, name))

def move_existing_files():
    with scandir(source_dir) as entries:
        for entry in entries:
            if not entry.is_file():
                continue
            name = entry.name
            if any(name.lower().endswith(ext) for ext in audio_extensions):
                move_files(dest_dir_audio, entry, name)
                logging.info(f"Moved audio file: {name} -> {dest_dir_audio}")
                
            elif any(name.lower().endswith(ext) for ext in video_extensions):
                move_files(dest_dir_video, entry, name)
                logging.info(f"Moved video file: {name} -> {dest_dir_video}")
                
            elif any(name.lower().endswith(ext) for ext in document_extensions):
                move_files(dest_dir_docs, entry, name)
                logging.info(f"Moved doc file: {name} -> {dest_dir_docs}")
                
            elif any(name.lower().endswith(ext) for ext in image_extensions):
                move_files(dest_dir_image, entry, name)
                logging.info(f"Moved image file: {name} -> {dest_dir_image}")
            
            elif any(name.lower().endswith(ext) for ext in app_extensions):
                move_files(dest_dir_apps, entry, name)
                logging.info(f"Moved application file : {name} -> {dest_dir_apps}")
            
            elif any(name.lower().endswith(ext) for ext in archive_extensions):
                move_files(dest_dir_zip, entry, name)
                logging.info(f"Moved zip file: {name} -> {dest_dir_zip}")

class FileManagementHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with scandir(source_dir) as entries:
            for entry in entries:
                if not entry.is_file():
                    continue
                name = entry.name
                self.check_for_audio_files(entry, name)
                self.check_for_document_files(entry, name)
                self.check_for_image_files(entry, name)
                self.check_for_video_files(entry, name)

    def check_for_audio_files(self, entry, name):
        if any(name.lower().endswith(ext) for ext in audio_extensions):
            move_files(dest_dir_audio, entry, name)
            logging.info(f"Moved audio file: {name}")

    def check_for_image_files(self, entry, name):
        if any(name.lower().endswith(ext) for ext in image_extensions):
            move_files(dest_dir_image, entry, name)
            logging.info(f"Moved image file: {name}")

    def check_for_video_files(self, entry, name):
        if any(name.lower().endswith(ext) for ext in video_extensions):
            move_files(dest_dir_video, entry, name)
            logging.info(f"Moved video file: {name}")

    def check_for_document_files(self, entry, name):
        if any(name.lower().endswith(ext) for ext in document_extensions):
            move_files(dest_dir_docs, entry, name)
            logging.info(f"Moved document file: {name}")
            
    def check_for_application_files(self, entry, name):
        if any(name.lower().endswith(ext) for ext in app_extensions):
            move_files(dest_dir_apps, entry, name)
            logging.info(f"Moved app file: {name}")
            
    def check_for_archive_files(self, entry, name):
        if any(name.lower().endswith(ext) for ext in archive_extensions):
            move_files(dest_dir_zip, entry, name)
            logging.info(f"Moved zip file: {name}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
    move_existing_files()
    
    event_handler = FileManagementHandler()
    observer = Observer()
    observer.schedule(event_handler, source_dir, recursive=False)
    observer.start()

    print("Watching folder... Press Ctrl+C to stop.")

    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
