# solution 1
import os

def get_files_in_folder(folder_path):
    files = os.listdir(folder_path)
    return files

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    return content

def read_text_file_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines

def read_binary_file(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()
    return content