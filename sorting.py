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


def selection_sort(lst: list, direction = 1):
    if direction == 1:
        for i in range(len(lst)):
            num_target = lst[i]
            num_idx = i
            for j in range(len(lst) - i):
                if (lst[j + i] <= num_target):
                    num_target = lst[j + i]
                    num_idx = i + j
            lst[i], lst[num_idx] = lst[num_idx], lst[i]
    else:
        for i in range(len(lst)):
            num_target = lst[i]
            num_idx = i
            for j in range(len(lst) - i):
                if (lst[j + i] >= num_target):
                    num_target = lst[j + i]
                    num_idx = i + j
            lst[i], lst[num_idx] = lst[num_idx], lst[i]
    return lst


def bubble_sort(lst: list, direction = 1):
    shuffled = True
    if direction == 1:
        while shuffled:
            shuffled = False
            for i in range(len(lst) - 1):
                if lst[i] > lst[i+1]:
                    lst[i], lst[i+1] = lst[i+1], lst[i]
                    shuffled = True
    else:
        while shuffled:
            shuffled = False
            for i in range(len(lst) - 1):
                if lst[i] < lst[i+1]:
                    lst[i], lst[i+1] = lst[i+1], lst[i]
                    shuffled = True
    return lst


def insertion_sort(lst: list, direction = 1):
    for i in range(len(lst) - 1):
        if (lst[i+1] < lst[i]):
            pom = lst[i+1]
            lst[i+1], lst[i] = lst[i], lst[i+1]
            for j in range(i-1):
                if (lst[i-j] > pom):
                    lst[i-j+1] = lst[i - j]
                    lst[i - j] = pom
                else:
                    break

    return lst


def main():
    data = read_data("numbers.csv")
    sorted_data = insertion_sort(data["series_1"], 0)
    print(sorted_data)
    pass


if __name__ == '__main__':
    main()
