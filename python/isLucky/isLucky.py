def isLucky(n):
    n_string = str(n)
    n_list = []

    is_zero = 0

    for digit in n_string:
        n_list.append(int(digit))

    half = len(n_list)/2

    for item in range(0, len(n_list)):
        if item < half:
            is_zero += n_list[item]
        else:
            is_zero -= n_list[item]

    return not is_zero


if __name__ == '__main__':
    print isLucky(1230)