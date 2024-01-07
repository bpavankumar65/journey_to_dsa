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


def sum_f_two(num_list, target):
    i = 0
    seen = {}
    list_of_subsets = []
    while i < len(num_list):
        complement = target - num_list[i]
        if complement in seen:
            print(complement, seen)
            list_of_subsets.append([(i, seen[complement])])
        seen[num_list[i]] = i
        print(i, len(num_list))
        i += 1
    return list_of_subsets

if __name__ == "__main__":
    print(sum_f_two([1,2,3,3,4,5,6], 6))
