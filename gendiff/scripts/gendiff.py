#!/usr/bin/env python3

import argparse

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

    print(f'Первый файл: {args.first_file}')
    print(f'Второй файл: {args.second_file}')
    print(f'Формат: {args.format}')

if __name__ == "__main__":
    main()