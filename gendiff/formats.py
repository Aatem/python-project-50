from gendiff.formatters.stylish import formatter_stylish as stylish
from gendiff.formatters.plain import formatter_plain as plain


def format(dictionary, formatter):
    if formatter == 'stylish':
        return stylish(dictionary)
    elif formatter == 'plain':
        return plain(dictionary)
    else:
        return 'Неизвестный форматтер!'
