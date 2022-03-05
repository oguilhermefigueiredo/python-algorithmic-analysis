
arr = []

def f(n):
    a, b = 0, 1

    for number in range(1, n):
        a, b = b, b + a
        arr.append(b)

def search(arr, target):
    for number in arr:
        if number == target:
            return number

    return -1

f(12)
print(search(arr, 40))
