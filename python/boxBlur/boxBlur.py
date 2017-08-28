def boxBlur(image):

    blur = [[0 for x in range(len(image[0]) - 2)] for y in range(len(image) - 2)]

    for i in range(1, len(image) - 1):
        for j in range(1, len(image[i]) - 1):
            blur_number = (image[i - 1][j - 1] +
                              image[i - 1][j] +
                              image[i - 1][j + 1] +
                              image[i][j - 1] +
                              image[i][j] +
                              image[i][j + 1] +
                              image[i + 1][j - 1] +
                              image[i + 1][j] +
                              image[i + 1][j + 1]
                              ) / 9

            blur[i - 1][j - 1] = blur_number

    return blur

if __name__ == '__main__':
    print boxBlur([[36,0,18,9],
                   [27,54,9,0],
                   [81,63,72,45]])
