def sum_of_elements(list_example):
    sum_list = 0
    mul_list = 1
    for x in list_example:
        sum_list += x
        mul_list *= x
    return sum_list, mul_list


def largest__of_list(list_example):
    largest = list_example[0]
    for i in range(len(list_example)):
        if largest < list_example[i]:
            largest = list_example[i]
    return largest


def largest_smallest_of_list(list_example):
    list_example.sort()
    return list_example[0], list_example[-1]


def count_same_ends(list_example):
    count = 0
    for elem in list_example:
        if elem[0] == elem[-1]:
            count += 1
    return count


def get_sorted_by_last_element(list_example):
    for _ in range(len(list_example)):
        for i in range(len(list_example) - 1):
            if list_example[i][1] > list_example[i + 1][1]:
                list_example[i + 1], list_example[i] = list_example[i], list_example[i + 1]
    return list_example


#### new solution
def last(n):
    return n[-1]


def get_sorted_by_last_element_smart(list_example):
    return sorted(list_example, key=last)
###################



if __name__ == "__main__":
    list_a = [0, -2, -3, 24, 20]
    list_str = ['abc', 'xyx', 'aba', '1221']
    sample_sorted = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    print("sum, mul,  are", sum_of_elements(list_a))
    print(largest_smallest_of_list(list_a))
    print(count_same_ends(list_str))
    print(get_sorted_by_last_element(sample_sorted))
    print(get_sorted_by_last_element_smart(sample_sorted))
