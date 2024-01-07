
def find_largest_common_prefix(list_ofthe_strings):
    shortest_string = min(list_of_strings, key=len)
    if list_ofthe_strings is None:
        return ''
    for i in range(len(shortest_string)):
        for elem in list_ofthe_strings:
            if elem[i] == shortest_string[i]:
                continue
            else:
                return shortest_string[:i]


def find_largest_prefix(str_list):
    if str_list is None:
        return ''
    shortest_string = min(str_list, key=len)
    for i, char in enumerate(str(shortest_string)):
        if str_list[0][i] != char:
            return shortest_string[:i]


if __name__ == "__main__":
    list_of_strings = ['pqrxyz', 'pqrabc', 'ps']
    print(find_largest_common_prefix(list_of_strings))
    print(find_largest_prefix(list_of_strings))
