
def allLongestStrings(inputArray):
    longest = 0
    longest_array = []

    for string in inputArray:
        if len(string) > longest:
            longest = len(string)
            longest_array = [string]
            continue

        if len(string) == longest:
            longest_array.append(string)

    return longest_array


if __name__ == '__main__':
    print allLongestStrings(["aba", "aa", "ad", "vcd", "aba"])
