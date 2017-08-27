def arrayChange(inputArray):
    count = 0

    for x in range(1, len(inputArray)):
        if inputArray[x - 1] >= inputArray[x]:
            count += inputArray[x-1] - inputArray[x] + 1
            inputArray[x] = inputArray[x-1] + 1

    return count

if __name__ == '__main__':
    print arrayChange([2, 3, 3, 5, 5, 5, 4, 12, 12, 10, 15])
