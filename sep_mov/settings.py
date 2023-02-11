input_path = "input/2023-02-11 15-35-24.mkv"
output_dir = "sep"
name = "test"

import os

def normalize_path(path):
    return os.path.normpath(os.path.abspath(path))

def get_settings():
    print(input_path)
    return normalize_path(input_path),normalize_path(output_dir),name
