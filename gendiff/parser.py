import json
import yaml
from yaml.loader import SafeLoader
import os


def get_data(file_path):
    _, ext = os.path.splitext(file_path)
    with open(file_path) as file:
        if ext == '.json':
            return parse(file, 'json')
        elif ext == '.yaml' or ext == '.yml':
            return parse(file, 'yaml')
        else:
            return 'Unknown format'


def parse(object, format):
    if format == 'json':
        return json.load(object)
    elif format == 'yaml':
        return yaml.load(object, Loader=SafeLoader)
