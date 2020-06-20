import argparse
from timeit import default_timer as timer


def get_n_sum(path: str = 'input.txt') -> int:
    file = open(path, 'r')

    ar = file.readline().rstrip().split(' ')
    return int(ar[2])


def get_lines_profit_price_arrays(path: str = 'input.txt') -> tuple:
    file = open(path, 'r')
    file.readline()

    result = ([], [], [])

    for line in file:
        row = line.rstrip().split(' ')
        count = int(row[3])
        price = int(float(row[2]) * 10)
        profit = count*(1000-price) + count*30
        if profit > 0:
            result[0].append(line)
            result[1].append(profit)
            result[2].append(price * count)

    return result


def get_mem_table(_profits: list, _prices: list, _cash: int) -> list:
    n = len(_profits)
    result = [[0] * (_cash + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for k in range(1, _cash + 1):
            if k >= _prices[i-1]:
                result[i][k] = max(result[i - 1][k], result[i - 1][k - _prices[i-1]] + _profits[i-1])
            else:
                result[i][k] = result[i - 1][k]

    return result


def get_best_combination_list(_mem_table: list, _prices: list, _cash: int, _lines: list) -> tuple:
    k = _cash
    result = []
    n = len(_lines)

    _total_profit = _mem_table[n][k]
    for i in range(n, 0, -1):
        if _mem_table[i][k] != _mem_table[i - 1][k]:
            result.insert(0, _lines[i-1])
            k -= _prices[i-1]

    return _total_profit, result


def create_output(_total_profit: int, _combination_list: list, path: str = 'output.txt'):
    with open(path, 'w') as file:
        file.write(str(_total_profit) + '\n')
        [file.write(x) for x in _combination_list]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Find max profit")
    parser.add_argument('-i', '--input', dest='input_filename', default='input.txt', help='input file name')
    parser.add_argument('-o', '--output', dest='output_filename', default='output.txt', help='output file name')
    args = parser.parse_args()

    start = timer()

    cash = get_n_sum(args.input_filename)
    lines, profits, prices = get_lines_profit_price_arrays(args.input_filename)

    mem_table = get_mem_table(profits, prices, cash)
    total_profit, combination_list = get_best_combination_list(mem_table, prices, cash, lines)
    create_output(total_profit, combination_list, args.output_filename)
    duration = timer() - start
    print(f"duration: %.3f seconds" % duration)



