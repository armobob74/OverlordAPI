"""
PVAR is a file format that allows for simple storage of variable information.
Its strength is that it's easy to parse using basic string utilities, even in languages where something like a JSON parser may not be available.

Here's an example:
item=apple
quantity=3
"""

def dict_to_pvar_string(d):
    lines = []
    for key in d:
        value = d[key]
        lines.append(f"{key}={value}")
    return '\n'.join(lines)

def pvar_string_to_dict(s):
    ret = {}
    lines = s.strip().split('\n')
    for line in lines:
        key, value = line.split('=')
        ret[key] = value
    return ret
