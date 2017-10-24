"""
A string is said to be beautiful if b occurs in it no more times than a; c occurs in it no more times than b; etc.

Given a string, check whether it is beautiful.

Example

For inputString = "bbbaacdafe", the output should be
isBeautifulString(inputString) = true;
For inputString = "aabbb", the output should be
isBeautifulString(inputString) = false;
For inputString = "bbc", the output should be
isBeautifulString(inputString) = false.
Input/Output

[time limit] 4000ms (py)
[input] string inputString

A string of lowercase letters.

Guaranteed constraints:
3 <= inputString.length <= 50.

[output] boolean
"""


def isBeautifulString(input_string):

    last_count = 50

    sort_string = sorted([x for x in input_string])

    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    last_letter = alphabet.index(sort_string[-1])

    to_the_last = alphabet[:last_letter + 1]

    for char in to_the_last:
        current_count = input_string.count(char)

        if current_count <= last_count:
            last_count = current_count
        else:
            return False

    return True


if __name__ == '__main__':
    print isBeautifulString("bbbaacdafe")
