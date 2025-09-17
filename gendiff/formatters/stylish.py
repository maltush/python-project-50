SEPARATOR = " "
INDENT_STEP = 4

ADD = '+ '
DEL = '- '
NONE = '  '


def format_value(value, spaces_count=2):
    if value is None:
        return "null"
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, dict):
        indent = SEPARATOR * (spaces_count + INDENT_STEP)
        lines = []
        for key, inner_value in value.items():
            formatted_value = format_value(inner_value, 
                                           spaces_count + INDENT_STEP)
            lines.append(f"{indent}{NONE}{key}: {formatted_value}")
        closing_indent = SEPARATOR * (spaces_count + INDENT_STEP - 2)
        return "{\n" + "\n".join(lines) + f"\n{closing_indent}}}"
    return str(value)


def make_stylish_diff(diff, spaces_count=2):
    lines = []
    indent = SEPARATOR * spaces_count
    
    for item in diff:
        key = item['name']
        action = item['action']
        value = format_value(item.get('value'), spaces_count)
        old_value = format_value(item.get('old_value'), spaces_count)
        new_value = format_value(item.get('new_value'), spaces_count)

        if action == "unchanged":
            lines.append(f"{indent}{NONE}{key}: {value}")
        elif action == "modified":
            lines.append(f"{indent}{DEL}{key}: {old_value}")
            lines.append(f"{indent}{ADD}{key}: {new_value}")
        elif action == "deleted":
            lines.append(f"{indent}{DEL}{key}: {old_value}")
        elif action == "added":
            lines.append(f"{indent}{ADD}{key}: {new_value}")
        elif action == 'nested':
            children = make_stylish_diff(item.get("children"), 
                                         spaces_count + INDENT_STEP)
            lines.append(f"{indent}{NONE}{key}: {children}")

    opening_brace = '{'
    closing_brace = SEPARATOR * (spaces_count - 2) + '}'
    return f"{opening_brace}\n" + "\n".join(lines) + f"\n{closing_brace}"


def format_diff_stylish(data):
    return make_stylish_diff(data)
