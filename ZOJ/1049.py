import math

N = raw_input()

for i in range(int(N)):
    vals = raw_input().split()
    X = float(vals[0])
    Y = float(vals[1])
    Z = (X * X + Y * Y) * math.pi / 100
    print("Property {}: This property will begin eroding in year {}.".format(i+1, int(Z)+1))

print("END OF OUTPUT.")
