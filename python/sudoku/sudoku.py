# coding=utf-8
"""
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with digits so that each column, each row,
and each of the nine 3 × 3 sub-grids that compose the grid contains all of the digits from 1 to 9.

This algorithm should check if the given grid of numbers represents a correct solution to Sudoku.

Example

For the first example below, the output should be true. For the other grid, the output should be false: each of the nine
3 × 3 sub-grids should contain all of the digits from 1 to 9.

Input/Output

[execution time limit] 4 seconds (py)

[input] array.array.integer grid

A matrix representing 9 × 9 grid already filled with numbers from 1 to 9.

[output] boolean

true if the given grid represents a correct solution to Sudoku, false otherwise.
"""

import numpy as np


def sudoku(grid):
    a = np.array(grid)
    b = a.transpose()

    one = a[0:3, 0:3].flatten().tolist()
    two = a[0:3, 3:6].flatten().tolist()
    three = a[0:3, 6:9].flatten().tolist()
    four = a[3:6, 0:3].flatten().tolist()
    five = a[3:6, 3:6].flatten().tolist()
    six = a[3:6, 6:9].flatten().tolist()
    seven = a[6:9, 0:3].flatten().tolist()
    eight = a[6:9, 3:6].flatten().tolist()
    nine = a[6:9, 6:9].flatten().tolist()

    for row in a.tolist():
        if len(set([x for x in row if row.count(x) > 1])) > 0:
            return False

    for row in b.tolist():
        if len(set([x for x in row if row.count(x) > 1])) > 0:
            return False

    if len(set([x for x in one if one.count(x) > 1])) > 0:
        return False

    if len(set([x for x in two if two.count(x) > 1])) > 0:
        return False

    if len(set([x for x in three if three.count(x) > 1])) > 0:
        return False

    if len(set([x for x in four if four.count(x) > 1])) > 0:
        return False

    if len(set([x for x in five if five.count(x) > 1])) > 0:
        return False

    if len(set([x for x in six if six.count(x) > 1])) > 0:
        return False

    if len(set([x for x in seven if seven.count(x) > 1])) > 0:
        return False

    if len(set([x for x in eight if eight.count(x) > 1])) > 0:
        return False

    if len(set([x for x in nine if nine.count(x) > 1])) > 0:
        return False

    return True


if __name__ == '__main__':
    print sudoku([[1,3,2,5,4,6,9,8,7],
                  [4,6,5,8,7,9,3,2,1],
                  [7,9,8,2,1,3,6,5,4],
                  [9,2,1,4,3,5,8,7,6],
                  [3,5,4,7,6,8,2,1,9],
                  [6,8,7,1,9,2,5,4,3],
                  [5,7,6,9,8,1,4,3,2],
                  [2,4,3,6,5,7,1,9,8],
                  [8,1,9,3,2,4,7,6,5]])