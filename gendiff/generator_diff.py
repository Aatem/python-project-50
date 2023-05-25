from gendiff.parser import get_data
from gendiff.tree import make_tree
from gendiff.formatters.stylish import style


def generate_diff(file1_path, file2_path, formatter='stylish'):
    file1 = get_data(file1_path)
    file2 = get_data(file2_path)
    dictionary = make_tree(file1, file2)
    result = style(dictionary)
    return result
