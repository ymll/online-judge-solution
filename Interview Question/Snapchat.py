# a = [1, 3 , 5 , 8, 10]
# b = [2, 7, 9, 11]
a =[]
b =[]

def merge(a ,b):
  c = []
  ptr1 = 0
  ptr2 = 0
  while ptr1 < len(a) or ptr2 < len(b):
#     print('ptr1: {}, ptr2: {}'.format(ptr1, ptr2))
    if ptr1 == len(a):
      c.append(b[ptr2])
      ptr2 += 1
    elif ptr2 == len(b):
      c.append(a[ptr1])
      ptr1 += 1
      # put the remaining elements to c
    elif a[ptr1] > b[ptr2]:
      c.append(b[ptr2])
      ptr2 += 1
    else:
      c.append(a[ptr1])
      ptr1 += 1
  return c

# print(merge(a, b))

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
# target = 16


total_length = len(matrix) * len(matrix[0])

def find_target(target):
  head = 0
  bottom = total_length - 1
  print(head, bottom)
  while head < bottom:
    middle = int((head + bottom) / 2) # 5 -> matrix[1][1]
    x = int ((middle + 1) / len(matrix[0]))
    y = int ((middle + 1) % len(matrix[0]) - 1) + 1
    print('middle: {}, x: {}, y: {}, matrix: {}'.format(middle, x, y, matrix[x][y]))
    if matrix[x][y] == target:
      return True
    elif  matrix[x][y] > target:
      bottom = middle - 1
    else:
      head = middle + 1
  print('head: {}, bottom: {}'.format(head, bottom))
  return False

print(find_target(0))
