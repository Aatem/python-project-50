def formatter_plain(diff):
    return make_plain(diff)[:-1]


def make_plain(diff, parent_path=''):
    children = diff.get('value')
    path = f"{parent_path}{diff.get('key', '')}"
    result = ''
    for child in children:
        string = ''
        type = child.get('type')
        if type == 'added':
            value = value_processing(child.get('value'))
            parent = f"{path}.{child.get('key')}".strip('.')
            string = f"Property '{parent}' was added with value: {value}\n"
            result += string
        elif type == 'unchanged':
            pass
        elif type == 'deleted':
            parent = f"{path}.{child.get('key')}".strip('.')
            string = f"Property '{parent}' was removed\n"
            result += string
        elif type == 'updated':
            value1 = value_processing(child.get('value1'))
            value2 = value_processing(child.get('value2'))
            parent = f"{path}.{child.get('key')}".strip('.')
            _ = f"Property '{parent}' was updated. From {value1} to {value2}\n"
            string = _
            result += string
        elif type == 'parent':
            line = list(make_plain(child, f"{path}."))
            string = ''.join(line)
            result += string
    return result


def value_processing(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, bool):
        return "true" if value else "false"
    elif value is None:
        return "null"
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return value