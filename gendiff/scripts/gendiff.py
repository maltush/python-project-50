#!/usr/bin/env python3

import argparse
import json


def read_json(file_path):
    with open(file_path, 'r') as file:
        a = file.read()
        return json.loads(a)


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        default='stylish',
        help='set format of output'
    )
    
    args = parser.parse_args()

    data1 = read_json(args.first_file)
    data2 = read_json(args.second_file)

    print(f'Первый файл: {args.first_file}')
    print(f'Второй файл: {args.second_file}')
    print(f'Формат: {args.format}')

    print(generate_diff(args.first_file, args.second_file))

    
def generate_diff(file_path1, file_path2):
    
    data1 = read_json(file_path1)
    data2 = read_json(file_path2)

    all_keys = sorted(set(data1.keys()) | set(data2.keys()))

    diff_lines = []

    for key in all_keys:

        if key not in data2:
            diff_lines.append(f"  - {key}: {json.dumps(data1[key], 
                                                       ensure_ascii=False)}")
        elif key not in data1:
            diff_lines.append(f"  + {key}: {json.dumps(data2[key], 
                                                       ensure_ascii=False)}")
        else:
            if data1[key] == data2[key]:
                diff_lines.append(f"    {key}: {json.dumps(data1[key], 
                                                           ensure_ascii=False)}")
            else:
                diff_lines.append(f"  - {key}: {json.dumps(data1[key], 
                                                           ensure_ascii=False)}")
                diff_lines.append(f"  + {key}: {json.dumps(data2[key], 
                                                           ensure_ascii=False)}")

    return "{\n" + "\n".join(diff_lines) + "\n}"


if __name__ == "__main__":
    main()