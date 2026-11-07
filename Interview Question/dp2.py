dp_table = [[]]
def precompute(map, m, n):
	for x in m:
		for y in n:
			if x-1 > 0:
				left = dp_table[x-1][y]
			else:
				left = 0
			if y-1 > 0:
				top = dp_table[x][y-1]
			else:
				top = 0
			if (x-1 > 0) and (y-1 > 0):
				top_left = dp_table[x-1][y-1]
			else:
				top_left = 0
			dp_table[x][y] = map[x][y] - top_left + top + left

def get_population(x1, y1, x2, y2):
	return dp_table[x2][y2] - dp_table[x1-1][y2] + dp_table[x1-1][y1-1] - dp_table[x2][y1-1]
