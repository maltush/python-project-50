import json
import os

import yaml


def get_file_format(file_path):
    _, extension = os.path.splitext(file_path)
    return extension[1:].lower()


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def parse_data(data, format):
    fmt = format.lower()
    if fmt == 'json':
        return json.loads(data)
    elif fmt in ('yaml', 'yml'):
        return yaml.safe_load(data)
    else:
        raise ValueError(f"Неподдерживаемый формат файла: {format}")


def parse_data_from_file(file_path):
    data = read_file(file_path)
    format = get_file_format(file_path)
    return parse_data(data, format)