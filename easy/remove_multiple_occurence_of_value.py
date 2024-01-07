def rem_multi_occurence(nums, value):
    l = nums.index(value)
    print(l)
    for r in range(l + 1, len(nums)):
        if nums[r] != value:
            print(nums[r])
            nums[l] = nums[r]
            l += 1
    print(nums[:l])


if __name__ == "__main__":
    l = [0, 1, 2, 2, 2, 3, 4, 2, 5]
    rem_multi_occurence(l, 2)
