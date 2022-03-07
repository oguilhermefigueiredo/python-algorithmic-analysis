
# Linear searching using just one ```if``` statement.
# Before I improve this code, a ```for``` loop was needed to go through every
# single item in the list, with a codition comparing the item with the target.
# With my solution, you just need one block of code the get the result, being
# more than 70% faster than the precedent solution.

arr = [1, 2, 3, 4, 5, 5, 5, 1, 2]

def search(arr, target):
    if target in arr:
        return target

    return -1

print(search(arr, 5))
