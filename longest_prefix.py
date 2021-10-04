"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""

Explanation: There is no common prefix among the input strings.
"""


def longest_prefix(arr):
    prefix = ""
    for letters in zip(*arr):
        if all(letters[0] == l for l in letters):
            prefix += letters[0]
        else:
            break

    return prefix


if __name__ == "__main__":
    assert longest_prefix(["flower","flow","flight"]) == "fl"
    assert longest_prefix(["dog","racecar","car"]) == ""
    assert longest_prefix(["cir","car"]) == "c"
