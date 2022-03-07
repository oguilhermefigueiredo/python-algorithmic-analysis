
# Convert string to list, taking every character as an item
string = 'hello there'

print(list(string))
# OUTPUT: ['h', 'e', 'l', 'l', 'o', ' ', 't', 'h', 'e', 'r', 'e']

# Transform a string into a list given a separator
arr = 'john:38912810'
arr = arr.split(':')

print(arr)
# OUTPUT: ['john', 38912810]

name, phone = arr

print('Name:', name, '\nPhone:', phone)
# OUTPUT:
#     Name: john
#     Phone: 38912810

# Using the items inside a list to create a new string
name = ['Hari', 'Seldon']
full_name = ' '.join(name)

print('Hello, %s!' %full_name)
# OUTPUT: Hello, Hari Seldon!

# Organizing a list into a crescent or decrescent order
numbers = [2, 10, 5, 4, 1, 9, 6, 3, 8, 7]

crescent = sorted(numbers)
print('crescent:', crescent)
# OUTPUT: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
decrescent = sorted(numbers, reverse=True)
print('decrescent:', decrescent)
# OUTPUT: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Copying lists to other variables
## Using the copy() method
l = [1, 2, 3, 4, 5]
ll = l.copy()

print(ll)
# OUTPUT: [1, 2, 3, 4, 5]

## Using slicing
lll = l[:]

print(lll)
# OUTPUT: [1, 2, 3, 4, 5]

## OBS: to point out to the same list in the memory, you can assign a new
## variable into the list and the changes will end in both, as you can use
## the same list on the memory to create different aliases to the same pointer
l = ll
l.append(6)

print(l)
# OUTPUT: [1, 2, 3, 4, 5, 6]
print(ll)
# OUTPUT: [1, 2, 3, 4, 5, 6]

lll = l.copy()
l.append(7)

print(l)
# OUTPUT: [1, 2, 3, 4, 5, 6, 7]
print(ll)
# OUTPUT: [1, 2, 3, 4, 5, 6, 7]
print(lll)
# OUTPUT: [1, 2, 3, 4, 5, 6]


