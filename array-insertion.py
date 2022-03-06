
arr = [1, 2, 3, 5]

def insert(arr, index, successor):
    for index in range(index, len(arr)):
        (arr[index], successor) = (successor, arr.insert(index, successor))

# def insert(arr, index, successor):
#     for index in range(index, len(arr)):
#     arr[4] = successor
#     arr.append(successor)
#     arr.insert(4, successor)


print('Array before insertion:', arr)
insert(arr, 3, -4)
print('Array after insertion:', arr)
