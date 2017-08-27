def addBorder(picture):
    picture_length = len(picture[0])
    frame_length = picture_length + 2
    cap = "*" * frame_length
    frame = [cap]

    for x in range(1, len(picture) + 1):
        frame.append("*" + picture[x - 1] + "*")

    frame.append(cap)

    return frame

if __name__ == '__main__':
    print addBorder(["abc", "ded"])