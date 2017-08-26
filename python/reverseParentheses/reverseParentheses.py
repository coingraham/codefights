def reverseParentheses(s):
    string_array = list(s)

    while "(" in string_array:

        inner_open = 0
        inner_close = 0

        for item in range(0, len(string_array)):
            if string_array[item] == "(":
                inner_open = item
            elif string_array[item] == ")":
                inner_close = item
                string_array = switchInner(string_array, inner_open, inner_close)
                break

    return ''.join([str(char) for char in string_array])

def switchInner(s, io, ic):
    s.pop(io)
    s.pop(ic-1)
    # print s[io:ic-1]
    # print s[ic-2:io-1: -1]
    s[io:ic-1] = s[ic-2:io-1: -1]

    return s


if __name__ == '__main__':
    print reverseParentheses("a(bc(de)f)g")