"""Given a string, output its longest prefix which contains only digits.

Example

For inputString="123aa1", the output should be
longestDigitsPrefix(inputString) = "123".

Input/Output

[time limit] 4000ms (py)
[input] string inputString

Guaranteed constraints:
3 <= inputString.length <= 35.

[output] string"""


def longestDigitsPrefix(inputString):

    answer = ""
    for char in inputString:
        if char.isdigit():
            answer += char
        else:
            break

    return answer

if __name__ == '__main__':
    print longestDigitsPrefix("123aa1")