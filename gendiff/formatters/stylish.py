def formatter_stylish(diff, depth=1):
    children = diff.get('value')
    type = diff['type']
    key = diff.get('key')
    index = '    ' * depth
    index_min = '    ' * (depth - 1)
    value = value_processing(diff.get('value'), depth)
    value1 = value_processing(diff.get('value1'), depth)
    value2 = value_processing(diff.get('value2'), depth)
    if type == 'root':
        line = map((lambda child: formatter_stylish(child, depth)), children)
        result = ''.join(line)
        return f'{{\n{result}}}'
    elif type == 'parent':
        line = map((lambda child: formatter_stylish(child, depth + 1)), value)
        result = ''.join(line)
        return f'{index}{key}: {{\n{result}{index}}}\n'
    elif type == 'added':
        return f'{index_min}  + {key}: {value}\n'
    elif type == 'deleted':
        return f'{index_min}  - {key}: {value}\n'
    elif type == 'unchanged':
        return f'{index_min}    {key}: {value}\n'
    elif type == 'updated':
        _ = f'{index_min}  - {key}: {value1}\n{index_min}  + {key}: {value2}\n'
        return _


def value_processing(value, depth):
    if isinstance(value, bool):
        return "true" if value else "false"
    elif value is None:
        return "null"
    elif isinstance(value, dict):
        index = '    ' * depth
        index_big = '    ' * (depth + 1)
        res = ''
        for k, v in value.items():
            res += f'\n{index_big}{k}: {value_processing(v, depth + 1)}'
        return f'{{{res}\n{index}}}'
    else:
        return value
