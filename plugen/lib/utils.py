import os

import yaml


def read_yaml_file(file_path):
    with open(file_path, 'r') as file:
        yaml_data = yaml.safe_load(file)
    return yaml_data

def list_recently_modified_files(directory, time):
    recent_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            modified_time = os.path.getmtime(file_path)

            if modified_time > time:
                recent_files.append(file_path)

    return recent_files