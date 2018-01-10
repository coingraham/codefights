def areSimilar(a, b):
    new_a = []
    new_b = []
    for x in range(len(a)):
        if a[x] != b[x]:
            new_a.append(a[x])
            new_b.append(b[x])

    return new_a == new_b or new_a == new_b[::-1]


if __name__ == '__main__':
    print areSimilar([832, 998, 148, 570, 533, 561, 894, 147, 455, 279],
                     [832, 998, 148, 570, 533, 561, 455, 147, 894, 279])
