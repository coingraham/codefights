def minesweeper(matrix):

    minesweep = [[0 for x in range(len(matrix[0]))] for y in range(len(matrix))]

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            count = 0

            try:
                if i - 1 >= 0 and j - 1 >= 0 and matrix[i - 1][j - 1]:
                    count += 1
            except:
                pass

            try:
                if i - 1 >= 0 and matrix[i - 1][j]:
                    count += 1
            except:
                pass

            try:
                if j - 1 >= 0 and matrix[i][j - 1]:
                    count += 1
            except:
                pass

            try:
                if i - 1 >= 0 and matrix[i - 1][j + 1]:
                    count += 1
            except:
                pass

            try:
                if j - 1 >= 0 and matrix[i + 1][j - 1]:
                    count += 1
            except:
                pass

            try:
                if matrix[i + 1][j]:
                    count += 1
            except:
                pass

            try:
                if matrix[i][j + 1]:
                    count += 1
            except:
                pass

            try:
                if matrix[i + 1][j + 1]:
                    count += 1
            except:
                pass

            minesweep[i][j] = count

    return minesweep


if __name__ == '__main__':
    print minesweeper([[True,False,False,True],
 [False,False,True,False],
 [True,True,False,True]])
