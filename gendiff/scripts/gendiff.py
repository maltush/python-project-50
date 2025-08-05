#!/usr/bin/env python3

import argparse
import json


def read_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


def generate_diff(data1, data2):
    if type(data1) is str:
        data1 = read_json(data1)
    if type(data2) is str:
        data2 = read_json(data2)
        
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff_lines = []

    for key in all_keys:
        if key not in data2:
            diff_lines.append(f"  - {key}: {json.dumps(data1[key], ensure_ascii=False)}")
        elif key not in data1:
            diff_lines.append(f"  + {key}: {json.dumps(data2[key], ensure_ascii=False)}")
        else:
            if data1[key] == data2[key]:
                diff_lines.append(f"    {key}: {json.dumps(data1[key], ensure_ascii=False)}")
            else:
                diff_lines.append(f"  - {key}: {json.dumps(data1[key], ensure_ascii=False)}")
                diff_lines.append(f"  + {key}: {json.dumps(data2[key], ensure_ascii=False)}")
    return "{\n" + "\n".join(diff_lines) + "\n}"


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('first_file', help='Path to the first JSON file')
    parser.add_argument('second_file', help='Path to the second JSON file')
    parser.add_argument(
        '-f', '--format',
        default='stylish',
        help='set format of output (default: stylish)'
    )

    args = parser.parse_args()
    
    # Теперь используем args внутри main()
    data1 = read_json(args.first_file)
    data2 = read_json(args.second_file)

    # Отладочная печать для проверки типов данных
    print(f"Тип данных первого файла ({args.first_file}): {type(data1)}")
    print(f"Тип данных второго файла ({args.second_file}): {type(data2)}")

    print(f'Первый файл: {args.first_file}')
    print(f'Второй файл: {args.second_file}')
    print(f'Формат: {args.format}')

    diff = generate_diff(data1, data2)
    print(diff)


if __name__ == "__main__":
    main()