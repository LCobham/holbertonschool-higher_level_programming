#!/usr/bin/python3
"""
    This module creates an executable that gives all possible solutions
    for the 'n-queen problem'.
"""
import sys


def main():
    argc = len(sys.argv)
    if (argc != 2):
        sys.stderr.write("Usage: nqueens N\n")
        sys.exit(1)

    try:
        queens = int(sys.argv[1])

    except Exception:
        sys.stderr.write("N must be a number\n")
        sys.exit(1)

    if queens < 4:
        sys.stderr.write("N must be at least 4\n")
        sys.exit(1)

    nQueens(queens)


def nQueens(n, P=[], depth=0):
    """Recursive function to solve the N-Queens problem using Backtracking"""
    if depth == n:
        print(P)
        return

    for i in range(n):
        result = P.copy()
        candidate = [depth, i]
        if GoodCandidate(result, candidate):
            result.append(candidate)
            nQueens(n, result, depth + 1)


def GoodCandidate(P, candidate):
    """Check that the new queen is not in conflict with  previous ones."""
    for i in range(len(P)):
        if P[i][0] == candidate[0] or P[i][1] == candidate[1]:
            return False

        xAxisDistance = candidate[0] - P[i][0]
        yAxisDistance = candidate[1] - P[i][1]
        if abs(xAxisDistance) == abs(yAxisDistance):
            return False

    return True


if __name__ == '__main__':
    main()
