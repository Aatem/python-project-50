from gendiff.formatters.stylish import format as stylish
from gendiff.formatters.plain import format as plain
from gendiff.formatters.json import format as json


def format(dictionary, formatter):
    if formatter == 'stylish':
        return stylish(dictionary)
    elif formatter == 'plain':
        return plain(dictionary)
    elif formatter == 'json':
        return json(dictionary)
    else:
        return 'Неизвестный форматтер!'
