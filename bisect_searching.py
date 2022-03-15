# Binary/bisect search algorithm
# It takes a list and a target value as arguments

arr = [40, 70, 10, 0, 100, 30, 80]

def bisect(list, target):
    list.sort()
    middle_index = (len(list) - 1) // 2
    middle_value = (list[-1] - list[0]) / 2
    
    if target == list[middle_index]:
        return True

    def searching():
        if target <= middle_value:
            for i in range(middle_index):
                if list[i] == target:
                    return True

        elif target > middle_value:
            for i in range(middle_index, len(list)):
                if list[i] == target:
                    return True
            	     
        return False

    return searching()
    

print(bisect(arr, 0))
# OUTPUT: True
print(bisect(arr, 50))
# OUTPUT: False
print(bisect(arr, 70))
# OUTPUT: True
