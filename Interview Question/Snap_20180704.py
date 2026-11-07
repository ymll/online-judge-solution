# Enter your code here. Read input from STDIN. Print output to STDOUT

# 2) given two sorted array of integers, find the median

def find_median(m, n):
    total_length = len(m) + len(n) - 2
    if total_length == 0:
        return None
    median_ptr = total_length / 2
    if total_length % 2 == 0:
        # length is even number
        median_ptr_2 = total_length / 2 + 1
    else:
        # length is odd number
        median_ptr_2 = total_length / 2

    answer = None
    m_ptr = 0
    n_ptr = 0
    while (m_ptr + n_ptr) < median_ptr_2:
        if m_ptr == len(m):
            n_ptr += 1
            answer = n[n_ptr]
            continue
        if n_ptr == len(n):
            m_ptr += 1
            answer = m[m_ptr]
            continue
        if m[m_ptr] < n[n_ptr]:
            m_ptr += 1
            answer = m[m_ptr]
        else:
            n_ptr += 1
            answer = n[n_ptr]
    
    return answer
    
    # if total_length % 2 == 0:
    #     # length is even number
        
    # else:
    #     # length is odd number
    #     median_ptr = total_length / 2

m = [1, 3, 4, 5]
n = [2 ,6, 7]
# 1, 2, 3, 4 , 5, 6 ,7, 8

print(find_median(m, n))






















# array of integers, e.g. a = [1, 3, 5, 6 10, 30, 5, 6, 7, 2], 1) find the max element
# import unittest


# def find_max(a):
#     # m = None
#     if not a:
#         return None
#     for i in a:
#         if m is None:
#             m = i
#         if i > m:
#             m = i
#     return m
    
# # a = [1, 3, 5, 6, 10, 30, 5, 6, 7, 2]
# a = []
# print(find_max(a))


# class TestFindMax(unittest.TestCase):
#     def test_all_positive_number(self):
#         a = [1, 2, 3, 4, 5]
#         expected = 5
#         actual = find_max(a)
#         self.assertEqual(expected, actual)
    
#     def test_all_negative_number(self):
#         a = [-1, -2, -3, -4, -5]
#         expected = -1
#         actual = find_max(a)
#         self.assertEqual(expected, actual)
        
#     def test_null_input(self):
#         a = []
#         expected = None
#         actual = find_max(a)
#         self.assertEqual(expected, actual)
        
#     def test_zero(self):
#         a = [0]
#         expected = 0
#         actual = find_max(a)
#         self.assertEqual(expected, actual)
        
# unittest.main()
