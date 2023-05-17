import json


def generate_diff(file1, file2):
    file_1 = json.load(open(file1))
    file_2 = json.load(open(file2))
    res = {}
    temp_dict = {}
    e = {}
    r = {}
    t = {}
    u = []
    result = ''
    for key in file_1.keys() - file_2.keys():
        res[' - ' + key] = file_1[key]
        temp_dict[key] = file_1[key]
    for key in file_2.keys() - file_1.keys():
        res[' + ' + key] = file_2[key]
        temp_dict[key] = file_2[key]
    for key in file_1.keys() - temp_dict.keys():
        e[key] = file_1[key]
    for key in file_2.keys() - temp_dict.keys():
        r[key] = file_2[key]
    for key in e.keys():
        for n in r.keys():
            if key == n:
                if e[key] != r[n]:
                    t[' - ' + key] = e[key]
                    t[' + ' + key] = r[key]
                if e[key] == r[n]:
                    t['   ' + key] = e[key]
    res.update(t)
    a = sorted(res, key=lambda x: x[2:])
    for key in a:
        for n in res.keys():
            if key == n:
                o = key + ': ' + str(res[n])
                u.append(o)
    for key in u:
        result += str(key) + '\n'
    result = '{\n' + result + '}'
    return result
