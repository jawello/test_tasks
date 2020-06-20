import argparse
import random
from datetime import datetime
from faker import Faker


random.seed(datetime.now())
fake = Faker()


class DataGenerator:
    def __init__(self,
                 days_count: int,
                 max_lots_day: int,
                 cash: int,
                 min_price: int = 500,
                 max_price: int = 1100,
                 min_count: int = 1,
                 max_count: int = 10,
                 input_filename: str = 'input.txt'):
        self.min_price: int = min_price
        self.max_price: int = max_price
        self.min_count: int = min_count
        self.max_count: int = max_count
        self.max_lots_day = max_lots_day
        self.days_count = days_count
        self.cash = cash
        self.input_filename = input_filename

    def __generate_lot(self) -> str:
        name = fake.bs().replace(' ', '_')
        price = random.randint(self.min_price, self.max_price) / 10
        count = random.randint(self.min_count, self.max_count)
        result = f"""{name} {price:.1f} {count}"""
        return result

    def __generate_day(self, day: int) -> list:
        result = []
        count_day = random.randint(1, self.max_lots_day)
        for _ in range(0, count_day):
            result.append(f"""{day} {self.__generate_lot()}\n""")
        return result

    def generate_data(self):
        with open(self.input_filename, 'w') as f:
            f.write(f"""{self.days_count} {self.max_lots_day} {self.cash}\n""")
            for i in range(1, self.days_count + 1):
                for item in self.__generate_day(i):
                    f.write(item)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate input data")
    parser.add_argument('days_count', type=int, help='Days count for data generation')
    parser.add_argument('max_lots_day', type=int, help='Max Lots count in one day')
    parser.add_argument('cash', type=int, help='How much money trader have')
    parser.add_argument('-i', '--input', dest='input_filename', default='input.txt', help='input file name')

    args = vars(parser.parse_args())
    gen = DataGenerator(**args)
    gen.generate_data()
