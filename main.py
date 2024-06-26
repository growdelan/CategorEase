"""Main runtime file"""

import time
from functions import utils
from functions.ollama import model_response


def create_directories(download_path):
    """Create directories if they don't exist"""
    dir_list = [
        "musics",
        "documents",
        "installations",
        "datas",
        "images",
        "videos",
        "archives",
    ]
    utils.create_directories(download_path, dir_list)


def handle_files(download_path):
    """Classification of files into appropriate directories using AI"""
    files = utils.get_file_names(download_path)
    print("Files: ", files)
    for file_name in files:
        print("File name: ", file_name)
        target_dir = model_response(model="llama3", file_name=file_name)
        print("Target dir: ", target_dir)
        source = utils.join_paths(download_path, file_name)
        print("Source: ", source)
        target = utils.join_paths(download_path, target_dir.lower())
        print("Target: ", target)
        response = utils.move_file(source, target)
        print(f"{response}/{file_name}")


def main():
    """main function"""
    download_path = "/Users/gohan/Downloads"
    create_directories(download_path)
    while True:
        handle_files(download_path)
        time.sleep(10)


if __name__ == "__main__":
    main()
