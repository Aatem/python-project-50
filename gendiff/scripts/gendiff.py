import argparse
from gendiff.generator_diff import generate_diff


parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.'
    )

parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument("-f", "--format", default='stylish',
                    help='set format of output',)

args = parser.parse_args()

print(args)


def main():
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
