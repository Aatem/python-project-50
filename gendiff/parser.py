import json
import yaml
from yaml.loader import SafeLoader
import os


def pars(file1, file2):
    _, ext1 = os.path.splitext(file1)
    _, ext2 = os.path.splitext(file2)
    if ext1 == '.yml' and ext2 == '.yml':
        file_1 = yaml.load(open(file1), Loader=SafeLoader)
        file_2 = yaml.load(open(file2), Loader=SafeLoader)
    elif ext1 == '.yaml' and ext2 == '.yaml':
        file_1 = yaml.load(open(file1), Loader=SafeLoader)
        file_2 = yaml.load(open(file2), Loader=SafeLoader)
    elif ext1 == '.json' and ext2 == '.json':
        file_1 = json.load(open(file1))
        file_2 = json.load(open(file2))
    return file_1, file_2
