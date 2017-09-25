"""
Find the leftmost digit that occurs in a given string.

Example

For inputString = "var_1__Int", the output should be
firstDigit(inputString) = '1';
For inputString = "q2q-q", the output should be
firstDigit(inputString) = '2';
For inputString = "0ss", the output should be
firstDigit(inputString) = '0'.
Input/Output

[time limit] 4000ms (py)
[input] string inputString

A string containing at least one digit.

Guaranteed constraints:
3 <= inputString.length <= 10.

[output] char
"""


def firstDigit(s):

    return [c for c in s if c.isdigit()][0]


def firstDigit2(inputString):

    # Top Python2 Answer
    return filter(lambda c: c.isdigit(), inputString)[0]

if __name__ == '__main__':
    print firstDigit("var_1__Int")