def format_value(value):
   
    type_handlers = {
        dict: lambda v: '[complex value]',
        list: lambda v: '[complex value]',
        type(None): lambda v: 'null',
        bool: lambda v: str(v).lower(),
        str: lambda v: f"'{v}'"
    }

    for data_type, handler in type_handlers.items():
        if isinstance(value, data_type):
            return handler(value)
    return str(value)


def make_plain_item(item, path=''):
    key = item.get('name')
    action = item.get('action')
    new_value = format_value(item.get('new_value'))
    old_value = format_value(item.get('old_value'))
    current_path = f"{path}.{key}" if path else key

    messages = {
        'added': f"Property '{current_path}' was added with value: {new_value}",
        'deleted': f"Property '{current_path}' was removed",
        'modified': (
            f"Property '{current_path}' was updated. "
            f"From {old_value} to {new_value}"
        )
    }

    if action in messages:
        return messages[action]
    elif action == 'nested':
        children = item.get('children')
        return make_plain_diff(children, current_path)
    return None


def make_plain_diff(diff, path=''):
    return '\n'.join(
        make_plain_item(item, path)
        for item in diff
        if make_plain_item(item, path) is not None
    )


def format_diff_plain(diff):
    return make_plain_diff(diff)