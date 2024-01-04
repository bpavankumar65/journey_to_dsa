def sum_of_elements(list_example):
    sum_list = 0
    mul_list = 1
    for x in list_example:
        sum_list += x
        mul_list *= x
    return sum_list, mul_list


def largest_smallest_of_list(list_example):
    list_example.sort()
    return list_example[0], list_example[-1]


if __name__ == "__main__":
    list_a = [-11, 200, 3, 4, 5]
    print("sum, mul,  are", sum_of_elements(list_a))
    print(largest_smallest_of_list(list_a))
