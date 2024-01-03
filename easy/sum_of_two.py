# sum of two numbers

# my-solution
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for var in range(len(nums)):
#             for x in range(len(nums)):
#                 if x != var:
#                     if target == (nums[var]+nums[x]):
#                         return [var, x]


class Solution:
    def twoSum(self, nums, target):
        seen = {}
        i = 0
        while i < len(nums):
            num = nums[i]
            complement = target - num
            if complement in seen:
                return [i, seen[complement]]
            seen[num] = i
            i += 1
