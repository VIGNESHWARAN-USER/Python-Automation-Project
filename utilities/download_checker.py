import os
import time

DOWNLOAD_DIR = os.path.join(os.getcwd(), "downloads")


def clear_downloads():
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)

    for file in os.listdir(DOWNLOAD_DIR):
        file_path = os.path.join(DOWNLOAD_DIR, file)

        if os.path.isfile(file_path):
            os.remove(file_path)


def is_file_downloaded(extension, timeout=15):

    end_time = time.time() + timeout

    while time.time() < end_time:

        files = os.listdir(DOWNLOAD_DIR)

        for file in files:
            if file.endswith(extension):
                return True

        time.sleep(1)

    return False