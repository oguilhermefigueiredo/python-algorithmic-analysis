
####
# This was an algorithm from a repository about Data Structure, where you needed
# to found a solution to inserting new elements inside a list. The solution used
# there isn't so good, so I did, after an entire weekend, the 10 lines of code
# needed in the function to just two, as you can see below. 
# That single expression inside the loop is sufficient to replace the element
# localized in an index to another and then put back the last element in the
# next index, doing it until all items in the iterable are available during
# the iterations.
####
# After my experience solving that issue, I fall in love with the language, as
# it allowed me to get involved in computational problems without having a
# massive experience with the language. And more than that: I realize how
# powerful is that language to manage data, and why the majority of the jobs in
# Data Science require python as the default technology.
####
# The repository have more than 7.2k of stars, and you can access my
# contribution using the link above:
# https://bit.ly/3IJD4PL
####

arr = [1, 2, 3, 5]

def insert(arr, index, successor):
    for index in range(index, len(arr)):
        (arr[index], successor) = (successor, arr.insert(index, successor))
        break

print('Array before insertion:', arr)
# OUTPUT: [1, 2, 3, 5]
insert(arr, 3, -4)
print('Array after insertion:', arr)
# OUTPUT: [1, 2, 3, -4, 5]
