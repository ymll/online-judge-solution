import sys
import functools

@functools.lru_cache(None)
def get_cycle_length(n, count = 1):
    if n == 1:
        return count
    if n % 2:
        return get_cycle_length(3 * n + 1, count + 1)
    else:
        return get_cycle_length(n / 2, count + 1)

sys.setrecursionlimit(1500)

while True:
    try:
        vals = input().split()
        i = int(vals[0])
        j = int(vals[1])
        max_l = 0
        for n in range( min(i,j), max(i,j)+1):
            l = get_cycle_length(n)
            if l > max_l:
                max_l = l
        print("{} {} {}".format(i, j, max_l))
    except EOFError:
        break

#print(get_cycle_length.cache_info())
