"""
Determine if the given character is a digit or not.

Example

For symbol = '0', the output should be
isDigit(symbol) = true;
For symbol = '-', the output should be
isDigit(symbol) = false.
Input/Output

[time limit] 4000ms (py)
[input] char symbol

A character which is either a digit or not.

[output] boolean

true if symbol is a digit, false otherwise.
"""

import re


def isDigit(symbol):

    regex = r"^\d$"

    return bool(re.search(regex, symbol))


if __name__ == '__main__':
    print isDigit("0")
