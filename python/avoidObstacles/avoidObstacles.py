def avoidObstacles(inputArray):

    for x in range(2, 42):
        local = []

        for number in inputArray:
            if number % x == 0:
                local.append(False)
            else:
                local.append(True)

        if False not in local:
            return x


if __name__ == '__main__':
    print avoidObstacles([5, 3, 6, 7, 9])

