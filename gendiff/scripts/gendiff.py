#!/usr/bin/env python3

import argparse

def main():
    parser = argparse.ArgumentParser(
        description='Generate diff between two files'
    )
    
    args = parser.parse_args()

    
    print("Это точка входа для gendiff")

if __name__ == "__main__":
    main()

import argparse
parser = argparse.ArgumentParser(description='Описание вашей программы')
parser.print_help()