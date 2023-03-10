import argparse
from gendiff.gendiff import generate_diff


def cli(argument=None):
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')

    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)

    parser.add_argument('-f', '--format', metavar='',
                        choices=['stylish', 'plain', 'json'], default='stylish',
                        help='output format (default: "stylish")')

    args = parser.parse_args(argument)
    return generate_diff(args.first_file, args.second_file, args.format)
