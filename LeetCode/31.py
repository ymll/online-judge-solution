import sys

class Solution:
    def swap(self, nums, a, b):
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp
        return nums
    
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        value = nums[-1]
        idx = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[i-1]: #5>3
                value = nums[i-1] # 5
                idx = i-1
                break
        if idx != -1:
            next_small = sys.maxsize
            next_small_index = len(nums)-1
            # find the smallest integer which is > temp
            for j in range(len(nums)-1, idx, -1):
                if nums[j] > value and nums[j] < next_small:
                    next_small = nums[j]
                    next_small_index = j
            if next_small >= value:
                self.swap(nums, idx, next_small_index) 
#        print('idx: {}, end:{}'.format(idx+1, int((len(nums)+idx)/2)+1))
        right_ptr = len(nums) - 1
        for j in range(idx+1, int((len(nums)+idx)/2)+1):
#            print('swap: {} and {}'.format(j, right_ptr))
            nums = self.swap(nums, j, right_ptr)
            right_ptr -= 1

#        print(nums)
