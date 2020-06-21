import argparse
from timeit import default_timer as timer


def get_share_sum(path: str = 'input.txt') -> tuple:
    result = []
    _sum_shares = 0
    with open(path, 'r') as file:
        file.readline()
        for line in file:
            share = float(line.strip())
            result.append(share)
            _sum_shares = _sum_shares + share
    return result, _sum_shares


def create_output(_shares: list, _sum_share: float, path: str = 'input.txt'):
    with open(path, 'w') as file:
        for share in _shares:
            file.write(f"""{share / _sum_share:.3f}\n""")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Find percentage share")
    parser.add_argument('-i', '--input', dest='input_filename', default='input.txt', help='input file name')
    parser.add_argument('-o', '--output', dest='output_filename', default='output.txt', help='output file name')
    args = parser.parse_args()

    start = timer()
    shares, sum_shares = get_share_sum(args.input_filename)
    create_output(shares, sum_shares, args.output_filename)
    duration = timer() - start
    print(f"duration: %.3f seconds" % duration)

