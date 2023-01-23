#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        length = len(matrix[i])
        if length > 0:
            for j in range(length):
                if j != length - 1:
                    print("{:d}".format(matrix[i][j]), end=' ')
                else:
                    print("{:d}".format(matrix[i][j]))
        else:
            print("")
