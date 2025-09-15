from gendiff.formatters.json_formatter import format_diff_json
from gendiff.formatters.plain import format_diff_plain
from gendiff.formatters.stylish import format_diff_stylish


def format_identifier(diff, formatter='stylish'):
    formatters = {
        'stylish': format_diff_stylish,
        'plain': format_diff_plain,
        'json': format_diff_json
    }
    try:
        return formatters[formatter](diff)
    except KeyError:
        raise ValueError(f"Unsupported formatter: {formatter}")
    
