def get_pairs_O_n_log_n_solution(lst, k):
    lst.sort()
    solution = []
    left_ptr = 0
    right_ptr = len(lst)-1
    while right_ptr > left_ptr:
        sum = lst[left_ptr] + lst[right_ptr]
        if sum < k:
            left_ptr += 1
        if sum > k:
            right_ptr -= 1
        if sum == k:
            solution.append((lst[left_ptr], lst[right_ptr]))
            right_ptr -= 1
    return solution


def get_pairs(lst, k):
    solution = []
    for idx, x in enumerate(lst):
        for n in range(len(lst)-1): # 0 - 3
            y = lst[len(lst)-n-1]
            if x + y == 15:
                solution.append((x, y))
    return solution


lst = [4, 5, 8, 7, 10]
k = 15

print(get_pairs(lst, k))
print(get_pairs_O_n_log_n_solution(lst, k))
