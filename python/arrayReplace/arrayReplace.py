def arrayReplace(inputArray, elemToReplace, substitutionElem):

    for item in range(len(inputArray)):
        if inputArray[item] == elemToReplace:
            inputArray[item] = substitutionElem

    return inputArray

if __name__ == '__main__':
    print arrayReplace([1, 2, 1], 1, 3)