import itertools
from gendiff.make_str import make_str

INDENT = 4
DEPTH_LINE = ' ' * INDENT
LVL = 1
RM = '  - '
ADD = '  + '


def stylish(tree: list) -> str:
    return build(tree)


def build(node, depth=0):
    if not isinstance(node, list):
        return make_str(node)

    deep_size = DEPTH_LINE * depth
    result = []

    for index in node:
        name = list(index.keys())[0]
        value = index[name]['value']
        status = refactor(index[name]['status'])

        if status == 'updated':
            result.append(f'{deep_size}{RM}{name}:'
                          f' {build(value[0], depth + LVL)}')
            result.append(f'{deep_size}{ADD}{name}:'
                          f' {build(value[1], depth + LVL)}')

        else:
            result.append(f'{deep_size}{status}{name}:'
                          f' {build(value, depth + LVL)}')

    return '\n'.join(itertools.chain('{', result, [deep_size + '}']))


def refactor(status):
    if status == 'added':
        return ADD
    elif status == 'removed':
        return RM
    elif status == 'not_changed':
        return DEPTH_LINE
    elif status == 'nested':
        return DEPTH_LINE
    else:
        return status
