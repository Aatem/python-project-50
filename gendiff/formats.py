from gendiff.formatters.stylish import formatter_stylish as stylish
from gendiff.formatters.plain import formatter_plain as plain
from gendiff.formatters.json import formatter_json as json


def format(dictionary, formatter):
    if formatter == 'stylish':
        return stylish(dictionary)
    elif formatter == 'plain':
        return plain(dictionary)
    elif formatter == 'json':
        return json(dictionary)
    else:
        return 'Неизвестный форматтер!'
