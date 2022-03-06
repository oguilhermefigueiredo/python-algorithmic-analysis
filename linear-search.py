
arr = [1, 2, 3, 4, 5, 5, 5, 1, 2]

def f(n):
    a, b = 0, 1

    for number in range(1, n):
        a, b = b, b + a
        arr.append(b)

def search(arr, target):
    if target in arr:
        return target

    return -1


print(search(arr, 5))
