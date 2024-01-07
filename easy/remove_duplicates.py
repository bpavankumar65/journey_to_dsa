def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    length = len(nums)
    for index in range(length - 1, 0, -1):
        if nums[index] - nums[index - 1] == 0:
            nums[index - 1] = nums[index]
            nums.remove(nums[index - 1])

    print(nums)
    return len(nums)


def remove_duplicates_second(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    length = len(nums)
    for index in range(1, length):
        if nums[index] == nums[index - 1]:
            nums[index - 1] = nums[index]
    print(nums)

# preferred-approach

def remove_dup_third(nums):
    l = 1
    for r in range(1, len(nums)):
        if nums[r] != nums[r-1]:
            nums[l] = nums[r]
            l += 1
    print(l)



if __name__ == "__main__":
    list_of_strings = [1, 1, 2, 2, 3, 4]
    l_s = [0, 1, 2, 2, 2, 3, 4, 2, 5]
    print(removeDuplicates(nums=list_of_strings))
    remove_duplicates_second(list_of_strings)
    remove_dup_third(list_of_strings)
