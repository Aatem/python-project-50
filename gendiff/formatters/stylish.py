INDENT = '    '


def format(diff, depth=1):
    children = diff.get('value')
    node_type = diff['type']
    key = diff.get('key')
    index = INDENT * depth
    index_min = INDENT * (depth - 1)
    value = value_to_string(diff.get('value'), depth)
    value1 = value_to_string(diff.get('value1'), depth)
    value2 = value_to_string(diff.get('value2'), depth)
    if node_type == 'root':
        line = map((lambda child: format(child, depth)), children)
        result = ''.join(line)
        return f'{{\n{result}}}'
    elif node_type == 'parent':
        line = map((lambda child: format(child, depth + 1)), value)
        result = ''.join(line)
        return f'{index}{key}: {{\n{result}{index}}}\n'
    elif node_type == 'added':
        return f'{index_min}  + {key}: {value}\n'
    elif node_type == 'deleted':
        return f'{index_min}  - {key}: {value}\n'
    elif node_type == 'unchanged':
        return f'{index_min}    {key}: {value}\n'
    elif node_type == 'updated':
        _ = f'{index_min}  - {key}: {value1}\n{index_min}  + {key}: {value2}\n'
        return _


def value_to_string(value, depth):
    if isinstance(value, bool):
        return "true" if value else "false"
    elif value is None:
        return "null"
    elif isinstance(value, dict):
        index = INDENT * depth
        index_big = INDENT * (depth + 1)
        res = ''
        for k, v in value.items():
            res += f'\n{index_big}{k}: {value_to_string(v, depth + 1)}'
        return f'{{{res}\n{index}}}'
    else:
        return value
