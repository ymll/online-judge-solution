#subset = {}

def get_substring(s):
    substring = ''
    for idx, val in enumerate(s):
        if subset[idx]:
            substring += str(val)
    return substring

def print_subset(s, current_idx, flag):
    subset[current_idx] = flag
    # s = {0, 1, 2, 3, 4, 5}
    if current_idx != len(s)-1:
        print_subset(s, current_idx + 1, True)
        print_subset(s, current_idx + 1, False)
    else:
        # print the subset
        print(get_substring(s))

s = set([0, 1, 2, 3, 4, 4, 5, 4, 5])
subset = [None for i in range(len(s))]
print_subset(s, 0, True)
print_subset(s, 0, False)

