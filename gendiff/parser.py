import json
import yaml
from yaml.loader import SafeLoader
import os


def get_data(file_path):
    _, ext = os.path.splitext(file_path)
    file = open(file_path)
    if ext == '.json':
        return parse(file, 'json')
    elif ext == '.yaml' or ext == '.yml':
        return parse(file, 'yaml')
    else:
        return 'Неизвестный формат'


def parse(file, file_format):
    if file_format == 'json':
        return json.load(file)
    elif file_format == 'yaml':
        return yaml.load(file, Loader=SafeLoader)
