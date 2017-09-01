import time
start_time = time.time()
my_table = []

def maxProdInTable(table):
    print("--- Beginning %s seconds ---" % (time.time() - start_time))
    # size = len(table)
    # right_side = size - 1
    max_product = 0
    skip = []
    done = []

    if len(table) % 2 == 0:
        start_cell = len(table) - 1
    else:
        start_cell = len(table)

    print("--- Starting skip %s seconds ---" % (time.time() - start_time))
    # max_product, skip = getIndividualMax(table, 0, size - 1)

    # Get the individual max
    for x in xrange(0, len(table)):
        for y in xrange(0, len(table)):
            if table[x][y] > max_product:
                max_product = table[x][y]
            if table[x][y] == 0:
                skip.append([x, y])


    print("--- starting loops %s seconds ---" % (time.time() - start_time))
    for cell in range(start_cell, 1, -2):
        left_offset = cell/2
        right_offset = len(table) - left_offset

        if max_product >= (cell+cell-1) ** 3:
            break

        print("--- Inside loops %s seconds ---" % (time.time() - start_time))
        for n in xrange(left_offset, right_offset):
            for m in xrange(left_offset, right_offset):
                if [n, m] in skip:
                    continue

                if [n, m] in done:
                    continue

                done.append([n, m])

                for cross_iter in xrange(left_offset, 0, -1):

                    total_cross = 1

                    for x in xrange(n - cross_iter, n + cross_iter + 1):
                        if table[x][m] == 0:
                            break
                        if table[x][m] == 1:
                            continue

                        total_cross *= table[x][m]

                    for y in xrange(m - cross_iter, m + cross_iter + 1):
                        if table[n][y] == 0:
                            break
                        if table[n][y] == 1:
                            continue

                        total_cross *= table[n][y]

                    if total_cross / table[n][m] > max_product:
                        max_product = total_cross / table[n][m]
                        break

                for diag_iter in xrange(left_offset, 0, -1):

                    total_diag = 1

                    for x in xrange(-diag_iter, diag_iter+1):
                        if table[n+x][m+x] == 0:
                            break
                        if table[n+x][m+x] == 1:
                            continue

                        total_diag *= table[n+x][m+x]

                    for y in xrange(-diag_iter, diag_iter+1):
                        if table[n+y][m-y] == 0:
                            break
                        if table[n+y][m-y] == 1:
                            continue

                        total_diag *= table[n+y][m-y]

                    if total_diag / table[n][m] > max_product:
                        max_product = total_diag / table[n][m]
                        break

    print("--- Getting the Modulo %s seconds ---" % (time.time() - start_time))
    return max_product % 1000000007


# def getCrossProduct(table, n, m, offset, skip):
#
#     total_cross = 1
#
#     for x in xrange(n-offset, n+offset+1):
#         if table[x][m] == 0:
#             return 0
#         if table[x][m] == 1:
#             continue
#
#         total_cross *= table[x][m]
#
#     for y in xrange(m-offset, m+offset+1):
#         if table[n][y] == 0:
#             return 0
#         if table[n][y] == 1:
#             continue
#
#         total_cross *= table[n][y]
#
#     return total_cross / table[n][m]
#
#
# def getDiagonalProduct(table, n, m, offset, skip):
#
#     total_diag = 1
#
#     for x in xrange(-offset, offset+1):
#         if table[n+x][m+x] == 0:
#             return 0
#         if table[n+x][m+x] == 1:
#             continue
#
#         total_diag *= table[n+x][m+x]
#
#     for y in xrange(-offset, offset+1):
#         if table[n+y][m-y] == 0:
#             return 0
#         if table[n+y][m-y] == 1:
#             continue
#
#         total_diag *= table[n+y][m-y]
#
#     return total_diag / table[n][m]


if __name__ == '__main__':
    test = [[1 for x in range(75)] for y in range(75)]
    print maxProdInTable(test)

    print("--- All done %s seconds ---" % (time.time() - start_time))
    # print maxProdInTable([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #                       [1, 1, 3, 1, 1, 1, 1, 1, 1, 1],
    #                       [1, 2, 3, 2, 1, 1, 1, 1, 1, 1],
    #                       [1, 1, 3, 1, 1, 1, 1, 1, 1, 1],
    #                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])


    # print maxProdInTable([[0,0,0,0,3],
    #                       [0,3,0,3,0],
    #                       [0,0,3,0,0],
    #                       [0,3,0,1,0],
    #                       [3,0,0,0,0]])



