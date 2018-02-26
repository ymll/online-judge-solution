import sys

input = []
for line in sys.stdin:
    input.append(line)

total = 0.0
for i in input:
    total += float(i)

print "${}".format(round(total/12, 2))
