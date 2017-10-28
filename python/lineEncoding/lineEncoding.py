"""
Given a string, return its encoding defined as follows:

First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
for example, "aabbbc" is divided into ["aa", "bbb", "c"]
Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
for example, substring "bbb" is replaced by "3b"
Finally, all the new strings are concatenated together in the same order and a new string is returned.
Example

For s = "aabbbc", the output should be
lineEncoding(s) = "2a3bc".

Input/Output

[time limit] 4000ms (py)
[input] string s

String consisting of lowercase English letters.

Guaranteed constraints:
4 <= s.length <= 15.

[output] string

Encoded version of s.
"""


def lineEncoding(s):

    encoded_string = ""
    encoded_list = [{"letter": s[0], "value": 0}]

    for letter in s:
        if letter == encoded_list[-1]["letter"]:
            encoded_list[-1]["value"] += 1

        else:
            encoded_list.append({"letter": letter, "value": 1})

    for item in encoded_list:
        if item["value"] == 1:
            encoded_string += item["letter"]
        else:
            encoded_string += str(item["value"]) + item["letter"]

    return encoded_string


if __name__ == '__main__':
    print lineEncoding("aabbbc")
