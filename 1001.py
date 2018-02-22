import sys

for line in sys.stdin:
    vals = line.split()
    print int(vals[0]) + int(vals[1])
