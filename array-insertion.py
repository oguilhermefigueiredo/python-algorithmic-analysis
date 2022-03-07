
arr = [1, 2, 3, 5]

def insert(arr, index, successor):
    for index in range(index, len(arr)):
        (arr[index], successor) = (successor, arr.insert(index, successor))
        break

print('Array before insertion:', arr)
insert(arr, 1, -4)
print('Array after insertion:', arr)
