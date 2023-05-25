import json
import yaml
from yaml.loader import SafeLoader
import os


def get_data(file_path):
    _, ext = os.path.splitext(file_path)
    if ext == '.json':
        return json.load(open(file_path))
    elif ext == '.yaml' or ext == '.yml':
        return yaml.load(open(file_path), Loader=SafeLoader)
    else:
        return 'Неизвестный формат'
