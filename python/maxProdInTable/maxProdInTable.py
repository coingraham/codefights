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

def maxProdInTable3(t):
    import operator
    M = 10**9+7

    a = 0
    r,c = len(t), len(t[0])
    for i in range(r):
        for j in range(c):
            a = max(a,t[i][j])


    def check(i,j,k,d):
        if d == 0:
            d = [(1,0),(-1,0),(0,1),(0,-1)]
        else:
            d = [(-1,-1),(-1,1),(1,-1),(1,1)]
        output = []
        for a,b in d:
            aa,bb = i+k*a,j+k*b
            if 0 <= aa < r and 0 <= bb < c:
                output.append((aa,bb))
            else:
                return []
        return output

    for i in range(1,r-1):
        for j in range(1,c-1):
            k = 1
            temp = t[i][j]
            if temp > 0:
                while True:
                    tt = check(i,j,k,0)
                    if tt:
                        temp = reduce(operator.mul, [t[ii][jj] for ii,jj in tt], temp)
                        if temp == 0:
                            break
                    else:
                        break
                    a = max(a,temp)
                    k += 1
                k = 1
                temp = t[i][j]
                while True:
                    tt = check(i,j,k,1)
                    if tt:
                        temp = reduce(operator.mul, [t[ii][jj] for ii,jj in tt], temp)
                        if temp == 0:
                            break
                    else:
                        break
                    a = max(a,temp)
                    k += 1
    return a%M

def maxProdInTable4(table):
    r=0
    for i in range(len(table)):
        for j in range(len(table)):
            prod1=prod2=table[i][j]
            r=max(prod1,r)
            for k in range(1,min(1+min(i,j),len(table)-max(i,j))):
                prod1*=table[i+k][j]*table[i-k][j]*table[i][j-k]*table[i][j+k]
                prod2*=table[i+k][j+k]*table[i-k][j+k]*table[i+k][j-k]*table[i-k][j-k]
                r=max(r,prod1,prod2)
                if prod1 == 0 and prod2 == 0:
                    break
    return r%1000000007

if __name__ == '__main__':
    test = [[1 for x in range(400)] for y in range(400)]
    print maxProdInTable4(test)

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




