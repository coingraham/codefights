def alternatingSums(a):

    totals = [0, 0]

    for x in range(len(a)):
        even_odd = x % 2
        totals[even_odd] += a[x]

    return totals

if __name__ == '__main__':
    print alternatingSums([50, 60, 60, 45, 70])