#!/usr/bin/env python3

import argparse

def main():
    parser = argparse.ArgumentParser(
        description='Generate diff between two files'
    )
    parser.add_argument(
        '-h', '--help',
        action='help',
        default=argparse.SUPPRESS,
    )
    
    args = parser.parse_args()

    
    print("Это точка входа для gendiff")