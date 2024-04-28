"""Module providing all necessary tools """

import os
import shutil


def create_directories(dir_path: str, dir_list: list):
    """checks whether the directories exist"""
    directories = dir_list
    for directory in directories:
        if not os.path.exists(f"{dir_path}/{directory}"):
            os.makedirs(f"{dir_path}/{directory}")
            print(f"A directory has been created: {directory}")
        else:
            print(f"Directory {directory} already exists")


def get_file_names(directory_path):
    """gets file names from a directory"""
    contents = os.listdir(directory_path)
    file_names = [
        item
        for item in contents
        if os.path.isfile(os.path.join(directory_path, item)) and item != ".DS_Store"
    ]
    return file_names


def join_paths(download_path: str, new_filename: str):
    """joins paths together"""
    path = os.path.join(download_path, new_filename)

    return path


def move_file(source, destination):
    """moves file from source to destination"""
    shutil.move(source, destination)

    return f"File moved to: {destination}"
