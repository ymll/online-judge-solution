N = int(raw_input())

def check_ab_pairs(n, m):
    count = 0
    for a in range(1, n-1):
        for b in range(a + 1, n):
            mod = (a * a + b * b + m) % (a * b)
            if (mod == 0):
                count += 1
    return count

for i in range(0, N):
    raw_input() # blank line
    case = 0
    while True:
        case += 1
        line = raw_input().split()
        n, m = int(line[0]), int(line[1])
        if (n == m) and (m == 0):
            break
        print("Case {}: {}".format(case, check_ab_pairs(n, m)))
    if (i < N-1):
        print
