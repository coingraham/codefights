def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):

    if yourLeft == friendsLeft:
        return yourRight == friendsRight
    elif yourRight == friendsLeft:
        return yourLeft == friendsRight
    else:
        return False

if __name__ == '__main__':
    print areEquallyStrong(10, 15, 5, 20)