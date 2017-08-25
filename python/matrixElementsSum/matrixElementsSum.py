

def matrixElementsSum(matrix):
    total = 0
    ghost_positions = ["OK"] * len(matrix[0])

    for row in matrix:

        for item in range(0, len(row)):

            if ghost_positions[item] == "X":
                continue

            if row[item] == 0:
                del ghost_positions[item]
                ghost_positions.insert(item, "X")
                continue

            total += row[item]

    return total


if __name__ == '__main__':
    print matrixElementsSum([[0, 1, 1, 2], [0, 5, 0, 0], [2, 0, 3, 3]])
