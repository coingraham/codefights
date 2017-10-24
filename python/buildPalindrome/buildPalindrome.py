"""
Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.

Example

For st = "abcdc", the output should be
buildPalindrome(st) = "abcdcba".

Input/Output

[time limit] 4000ms (py)
[input] string st

A string consisting of lowercase latin letters.

Guaranteed constraints:
3 <= st.length <= 10.

[output] string
"""


def buildPalindrome(st):
    reverse_st = st[::-1]
    size = len(st)

    for x in range(0, size):
        string_slice = st[0 + x: size]
        reverse_slice = reverse_st[0: size - x]
        if string_slice == reverse_slice:
            return_slice = st + reverse_st[size - x:]
            return return_slice


if __name__ == '__main__':
    print buildPalindrome("abcdc")
