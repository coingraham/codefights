"""

"""


# answer by nemoy
def spiralNumbers(n, m=0, s=1):
    if m == 0: m = n
    if n == 1 == m:
        return [[s]]

    # Calculate spiral numbers without first row
    S = spiralNumbers(m - 1, n, s + n)

    # Create first row and add the transpose of the rest
    return [range(s, s + n)] + zip(*S[::-1])


# answer by lucky-seven
def spiralNumbers_alt(n):
    m = [[0] * n for i in range(n)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, c = 0, -1, 1
    for i in range(n + n - 1):
        for j in range((n + n - i) // 2):
            x += dx[i % 4]
            y += dy[i % 4]
            m[x][y] = c
            c += 1
    return m


if __name__ == '__main__':
    print spiralNumbers(3)
