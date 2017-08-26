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
                string_array[inner_open:inner_close + 1] = switchInner(string_array[inner_open:inner_close + 1])
                string_array.pop(inner_close)
                string_array.pop(inner_open)
                break

    return ''.join([str(char) for char in string_array])


def switchInner(substring):

    return substring[::-1]

if __name__ == '__main__':
    print reverseParentheses("(abcde)")
