example_list = [1, 2, 3, 4, 5, 6]
print(sorted(example_list))
example_list.sort()
print(example_list)

"""
sorted(list) returns a list of ascending or alphabetical
list.sort() mutates the list but it wont return anything , it return None
"""

example_list.extend([True, 9, 10, 2])
list1 = ["abc", "dfa"]
print(sorted(list1, key = lambda i:i[2], reverse=True))