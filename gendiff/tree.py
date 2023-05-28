def make_tree(data1, data2):
    return {'type': 'root', 'value': temp_tree(data1, data2)}


def temp_tree(data1, data2):
    result = []
    keys = data1.keys() | data2.keys()
    for key in sorted(keys):
        if key not in data1:
            result.append({
                'key': key,
                'type': 'added',
                'value': data2[key]
            })
        elif key not in data2:
            result.append({
                'key': key,
                'type': 'deleted',
                'value': data1[key]
            })
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            result.append({
                'key': key,
                'type': 'parent',
                'value': temp_tree(data1[key], data2[key])
            })
        elif data1[key] == data2[key]:
            result.append({
                'key': key,
                'type': 'unchanged',
                'value': data1[key]
            })
        else:
            result.append({
                'key': key,
                'type': 'updated',
                'value1': data1[key],
                'value2': data2[key]
            })
    return result
