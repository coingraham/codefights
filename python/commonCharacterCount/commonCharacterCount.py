

def commonCharacterCount(s1, s2):

    list_s1 = list(s1)
    list_s2 = list(s2)
    count = 0

    for item in list_s1:
        if item in list_s2:
            list_s2.remove(item)
            count += 1

    return count

if __name__ == '__main__':
    print commonCharacterCount("aabcc", "adcaa")