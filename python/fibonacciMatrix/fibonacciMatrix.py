def fibonacciMatrix(n):

    if n == 0:
        return []

    matrix = [[0 for x in range(n)] for y in range(n)]

    fib = [0, 1, 2, 4, 7, 12, 20, 33, 54, 88, 143, 232, 376]

    half = n/2

    matrix[half][half] = 1

    current = [half, half]

    for x in range(1, 12):

        # Go West
        if x % 4 == 1:
            right = current[1]
            for j in range(right, right - fib[x] - 1, -1):
                if j >= 0:
                    matrix[current[0]][j] = 1
                    current[1] = j
                else:
                    return matrix

        # Go North
        if x % 4 == 2:
            left = current[0]
            for i in range(left, left - fib[x] - 1, -1):
                if i >= 0:
                    matrix[i][current[1]] = 1
                    current[0] = i
                else:
                    return matrix

        # Go East
        if x % 4 == 3:
            right = current[1]
            for j in range(right, right + fib[x] + 1):
                try:
                    matrix[current[0]][j] = 1
                    current[1] = j
                except:
                    return matrix

        # Go South
        if x % 4 == 0:
            left = current[0]
            for i in range(left, left + fib[x] + 1):
                try:
                    matrix[i][current[1]] = 1
                    current[0] = i
                except:
                    return matrix

    return matrix


def fibonacciMatrix2(s):
    # Saw this interesting Matrix notation.  Testing it out.
    M = [s*[0] for n in [0]*s]

    # Step by step
    print s*[0]
    print [0]*s

    # Same so it can be written like this too
    M = [s*[0] for n in s*[0]]

    print M

if __name__ == '__main__':
    print fibonacciMatrix(2)
