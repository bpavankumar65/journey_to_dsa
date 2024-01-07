def remove_element_at_end(array_var, elem):
    return array_var[:len(array_var) - 1]


# Insert n into index i after shifting elements to the right.
# Assuming i is a valid index and arr is not full.
def insertMiddle(arr, i, n, length):
    # Shift starting from the end to i.
    for index in range(length - 2, i - 1, -1):
        print(index)
        arr[index + 1] = arr[index]

    # Insert at i
    arr[i] = n
    return arr


def removeMiddle(arr, i, n, length):
    # Shift starting from the end to i.
    for index in range(i + 1, length):
        print("index is", index, arr[index])
        arr[index - 1] = arr[index]
    return arr


def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    while val in nums:
        nums.remove(val)
    print(nums)






if __name__ == "__main__":
    array_var1 = [1, 2, 3, 4, 5, 6]
    array_var2 = [1, 2, 3, 4, 5, 6]
    array_var3 = [1, 2, 3, 3, 5, 4]
    print(remove_element_at_end(array_var1, 4))
    print(insertMiddle(array_var1, 2, 10, len(array_var1)))
    print(removeMiddle(array_var2, 2, 10, len(array_var2)))
    removeElement(array_var3, 3)
