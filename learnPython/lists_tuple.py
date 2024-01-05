# tuples
"""
tuples are immutable, indexed, can have all other collections like lists, set , dicct.

Abilities of tuple:
len(tuple) ------> gives number of elements in the tuple
tuple.count(element) --------> number of times the element appeared in the tuple
tuple.index(element) --------> gives the index of the element


iterating over tuples:

for i in tuple:
    gives ith element in the tuple

if element in tuple
    pass

can't do:

It is not possible to add or remove elements from a tuple; they are immutable
eventhough the tuple is sliced, a duplicate tuple is formed but the original tuple will be remained same
"""

tuple_var = (1, 2, 3, 4)
print(len(tuple_var))
print(tuple_var.count(4))
print(tuple_var.index(3))
var_2 = ('a', tuple_var)
print(var_2)
for x in var_2:
    test = var_2[:1]
    if x in test:
        print("got first element")
    else:
        print("not found for the second time")

######################################################################################################################

### Lists
"""
Lists are mutable, indexed, ordered
lists are arrays , can be iterable, sliced
lists can perform tuple actions like len(), count(tuple), index(tuple) along with also can modify lists like add, delete
inserting elements.

we can convert from tuple, dict, sets to list using list(collection)

index from left to right ------> 0 to len(list)-1
index from right to left -------> -1 to -(len(list)

Method Description
append() | Adds an element at the end of the list
clear()  | Removes all the elements from the list
copy()   | Returns a copy of the list
count()  | Returns the number of elements with the specified value
extend() | Add the elements of a list (or any iterable), to the end of the current list
index()  | Returns the index of the first element with the specified value
insert() | Adds an element at the specified position
pop()    | Removes the element at the specified position
remove() | Removes the item with the specified value
reverse()| Reverses the order of the list
sort()   | Sorts the list

"""

## slicing
list_var = [1, 2, 3, 4, 5, 6]
print(list_var[:])
print(list_var[::-1])
print("list_var[-1] is ", list_var[-1])
print("list_var[-2:2 is ", list_var[-2:2])
print(list_var[-3:-2])

# index from left to right ------> 0 to len(list)-1
# index from right to left -------> -1 to -(len(list)
print(list_var[0:len(list_var)])
print(list_var[-(len(list_var)):])

## adding to the list
list_var.append(7)
print(list_var)
list_var.extend([8, 9])
print(list_var)

## insertion
list_var.insert(2, 2)
print(list_var)

## list concatenation
list_two = [101, 102]
print(list_var + list_two)

## removing from list      removes an element from right
list_var.remove(2)
print(list_var)
print(list_var.index(4))
print(list_var.count(2))

print(list_var.pop())
print(list_var.pop(7))  # -----> pop gets index of the element and returns element present at the index
print(list_var)

## deleting from a list
del list_var[2] # its index
print(list_var)
list_var.remove(2) # its element
print(list_var)

## list methods
list_var.append(10)
print("append", list_var)
list_var.insert(4,11)
print("insert", list_var)
list_var.extend([12,13])
print("extend", list_var)
list_var.pop(5)
print("pop fn is ", list_var)
list_var.remove(12)
print("remove fn ", list_var)
list_var.reverse()
print("reverse", list_var)
list_var.sort()
print("sort", list_var)

