input_path = "input/test.mkv"
output_dir = 'sep'
name = "test"

import os

def normalize_path(path):
    return os.path.normpath(os.path.abspath(path))

def get_settings():
    print(input_path)
    return normalize_path(input_path),normalize_path(output_dir),name
