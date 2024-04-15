import os
import numpy as np
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    # print(file_path)
    data = np.genfromtxt(file_path, delimiter=',')
    with open(file_path, newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        keys = next(csv_reader)

    slovnik = {}
    # slovnik[tuple(data[0, :])] = data[1:, :]
    for i in range(data.shape[1]):
        slovnik[keys[i]] = list(data[1:, i])

    return slovnik




def main():
    data = read_data("numbers.csv")
    print(data)
    pass


if __name__ == '__main__':
    main()
