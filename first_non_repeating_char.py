"""
Return the first character that does not repeat anywhere in the input string.
If all characters are repeating, return 0
Example 1:
Input: 'noon'
Output: 0

Example 2:
Input: 'apple'
Output: 'a'

Example 3:
Input: 'kayak
Output: 'y'
"""
def first_non_repeating_char(string):
    occur = set()
    non_repeat_char = {}
    for pos in range(len(string)):
        c = string[pos]
        if c in occur:
            if c in non_repeat_char:
                non_repeat_char.pop(c)
        else:
            occur.add(c)
            non_repeat_char[c] = pos
    if not non_repeat_char:
        return 0
    first_char_pos = len(string)
    for key, value in non_repeat_char.items():
        if value < first_char_pos:
            first_char_pos = value
    return string[first_char_pos]
