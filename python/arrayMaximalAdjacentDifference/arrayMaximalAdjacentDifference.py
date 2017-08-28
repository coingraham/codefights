def arrayMaximalAdjacentDifference(inputArray):
    difference = 0
    for x in range(1, len(inputArray)):
        tmp = inputArray[x] - inputArray[x - 1]
        if tmp < 0:
            if (tmp * -1) > difference:
                difference = tmp * -1
        else:
            if tmp > difference:
                difference = tmp
    return difference

if __name__ == '__main__':
    print arrayMaximalAdjacentDifference([2, 4, 1, 0])