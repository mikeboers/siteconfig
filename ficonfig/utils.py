import re


def normalize_key(input_):
    input_ = re.sub(r'[^\w\[\]]+', '_', input_)
    input_ = re.sub(r'^(\w+)', lambda m: m.group(1).upper(), input_)
    return input_


def shell_escape(input_):
    return str(input_).replace('"',  '\\"')


def shell_quote(input_):
    return '"%s"' % shell_escape(input_)
