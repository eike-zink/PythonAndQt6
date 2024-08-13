import argparse
import pandas as pd


def read_date(file_name):
    return pd.read_csv(file_name)


if __name__ == '__main__':
    options = argparse.ArgumentParser()
    options.add_argument('-f', '--file', type=str, required=True, help="Name of the CSV-file")
    args = options.parse_args()
    data = read_date(args.file)
    print(data)
