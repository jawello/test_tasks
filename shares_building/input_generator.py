import argparse
import random
from datetime import datetime

random.seed(datetime.now())


def generate_data(_share_count: int, input_filename: str = 'input.txt'):
    with open(input_filename, 'w') as file:
        file.write(f"""{_share_count}\n""")
        for i in range(0, _share_count):
            file.write(f"""{random.uniform(0.1, 10):.1f}\n""")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate input data")
    parser.add_argument('shares_count', type=int, help='Shares count for data generation')
    parser.add_argument('-i', '--input', dest='input_filename', default='input.txt', help='input file name')

    args = parser.parse_args()
    generate_data(args.shares_count, args.input_filename)

