
arr = [1, 2, 3, 4, 5, 5, 5, 1, 2]

def search(arr, target):
    if target in arr:
        return target

    return -1


print(search(arr, 5))
