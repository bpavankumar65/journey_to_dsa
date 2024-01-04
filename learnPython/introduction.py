i = 2
my_name = 'pavan'

# strings

"""strings are immutable"""

print("Hello")
print('hello {}'.format(my_name))

"""Explore replacing a string
Create a string with words separated by ‘,’ and replace the commas with spaces;
for example replace all the commas in ‘Denyse,Marie,Smith,21,London,UK’
with spaces. Now print out the resulting string."""


name = 'Denyse,Marie,Smith,21,London,UK'
print(name.replace(",", " "))
first_name = "pavan"
second_name = "bandaru"
new_string = first_name + " " + second_name
print(new_string)
print("length of the str is {} ".format(len(new_string))) # length of the str is 13
print(new_string.upper()) # PAVAN BANDARU
print(new_string.find('ban')) # 6
print(new_string.replace("bandaru", "kumar")) # 'pavan kumar'
print(new_string.split(' ')) # ['pavan', 'bandaru']
print(new_string.count('a')) # 4
print(f'here is {new_string}') # here is pavan bandaru
x = 10.1234
print(f'{x:.2f}') # 10.12


# numbers and integers
#control flow
if "pavan" in new_string:
    print("pavan is there")
elif "van" in new_string:
    print("still pavan")
else:
    print(new_string)
# while

while(True):
    print('Navap')
    break

def try_while():
    count = 0
    dict = {}
    while(count<10):
        dict[str(count)] = 'a'
        count += 1
    dict['2'] = 'b'
    print(dict)

#try_while()

# for-loop
example_array = [10]*5
sample = {}
counter = 0
for i in example_array:
    sample[str(counter)] = i+1
    counter +=1
for _ in range(0,10):
    print('.', end='')
    print()


#for i in range(10, 0, -1): _________ prints 10,9,8,7,6,5,4,3,2,1,

print(sample)



