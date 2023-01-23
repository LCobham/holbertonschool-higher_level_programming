#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        length = len(matrix[i])
        for j in range(length):
            if j != length - 1:
                print("{}".format(matrix[i][j]), end=' ')
            else:
                print("{}".format(matrix[i][j]))
