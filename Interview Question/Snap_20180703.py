import string
'''
/***
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
*/

ân                      adaâ
'''


def is_palindrome(s):
    left_ptr = 0
    right_ptr = len(s) - 1
    while left_ptr < right_ptr:
        # create a set with a-z A-Z 0-9
        pattern = Set(string)
        pattern.add(string.letters)
        pattern.add(string.digits)
        if not pattern[s[left_ptr]]:
            left_ptr += 1
            continue
        if not pattern[s[right_ptr]]:
            right_ptr -= 1
            continue
        if s[left_ptr] == s[right_ptr]:
            left_ptr += 1
            right_ptr -= 1
        else:
            return False
    return True
    
    
    
    
    
    Given a string (all valid lowercase characters), every step you can delete/change one character at the beginning or the end of the string. Minimize the step number to make it a palindrome.

For example,
"abc" -> 1
"abac" -> 1
"abcd" -> 2


abcd -> bc -> cc 2


f(abcd)
f(abc) f(bcd) f(bc)



def get_step_number(s, step):
    if len(s) == 0 or len(s) == 1:
        return 0
#    if step == len(s):
#        return len(s) - 1
    if is_palindrome(s):
        return step
    remove_head = get_step_number(s[1:], step + 1)
    remove_tail = get_step_number(s[:-2], step + 1)
    remove_both = get_step_number(s[1:-2], step + 1)
    
    min_step = min(remove_head, remove_tail, remove_both)
    return min_step
