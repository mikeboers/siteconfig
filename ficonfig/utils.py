import re


def normalize_key(input_):
    return re.sub(r'\W+', '_', input_).upper()


def shell_escape(input_):
    return str(input_).replace('"',  '\\"')


def shell_quote(input_):
    return '"%s"' % shell_escape(input_)
