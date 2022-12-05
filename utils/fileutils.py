import os


def get_relative_file_path(file_name: str) -> str:
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', file_name))


def read_all_lines(file_name: str) -> str:
    cur_dir = os.path.dirname(__file__)
    input_path = os.path.join(cur_dir, file_name)
    input_file = open(input_path, 'r')
    return input_file.read()
