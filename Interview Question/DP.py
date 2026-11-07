def precompute(map, m, n):
#    dp_table = [[0]*n]*m
#    print(dp_table)
#    print(dp_table[0])
    dp_table = [[0] * n for i in range(m)]
    for x in range(m):
        for y in range(n):
            if x-1 >= 0:
                top = dp_table[x-1][y]
#                print("top = {} = dp_table[{}][{}]".format(top, x-1, y))
            else:
                top = 0
            if y-1 >= 0:
#                print("left = {} = dp_table[x][y-1] = dp_table[{}][{}]".format(dp_table[x][y-1], x, y-1))
                left = dp_table[x][y-1]
            else:
                left = 0
            if (x-1 >= 0) and (y-1 >= 0):
#                print("topleft = dp_table[{}][{}] = {}".format(x-1, y-1, dp_table[x-1][y-1]))
#                print(dp_table)
                top_left = dp_table[x-1][y-1]
            else:
                top_left = 0
#            print('map[{}][{}]:{} - topleft:{} + top:{} + left:{}'.format(x, y, map[x][y], top_left, top, left))
            dp_table[x][y] = map[x][y] - top_left + top + left
#            print('dp_table[{}][{}] = {}'.format(x,y, dp_table[x][y]))
    return dp_table

def get_population(dp_table, x1, y1, x2, y2):
    if y1-1 >= 0:
        top_square = dp_table[x2][y1-1]
    else:
        top_square = 0
    if x1-1 >= 0:
        left_square = dp_table[x1-1][y2]
    else:
        left_square = 0
    if left_square > 0 and top_square > 0:
        overlap = dp_table = [x1-1][y1-1]
    else:
        overlap = 0
    return dp_table[x2][y2] - left_square + overlap - top_square

map = []
map.append([1,1,1,1,1])
map.append([1,1,1,1,1])
map.append([1,1,1,1,1])
#map.append([1,2,3,4,5])
#map.append([1,2,3,4,5])
#map.append([1,2,3,4,5])
dp_table = precompute(map, 3, 5)
print(dp_table)
print(get_population(dp_table, 0, 2, 1, 2))
print(get_population(dp_table, 0, 0, 2, 2))
print(get_population(dp_table, 1, 2, 3, 2))
