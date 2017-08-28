import re

def isIPv4Address(inputString):

    ipv4_list = inputString.split(".")

    if re.search('[^\d|^\.]', inputString):
        return False

    dots = [m.start() for m in re.finditer('\.', inputString)]

    if len(dots) != 3:
        return False

    digits = [m.start() for m in re.finditer('\d', inputString)]

    if not 4 <= len(digits) <= 12:
        return False

    try:

        if len(ipv4_list) > 4:
            return False

        elif "" in ipv4_list:
            return False

        for sub in ipv4_list:

            if len(sub) > 3:
                return False

            if sub == "00" or sub == "000":
                return False

            if not 0 <= int(sub) < 256:
                return False
    except:

        return False

    return True

if __name__ == '__main__':
    print isIPv4Address(".100.200.100.200")
