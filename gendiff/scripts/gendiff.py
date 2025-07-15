#!/usr/bin/env python3

import argparse
import json

def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

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

if __name__ == "__main__":
    main()