def binary_search(list, target):
    '''
    Searches a target and returns target's index.
    Returns -1 if target was not found.
    Implemented in logarithmic time.
    '''
    left = 0
    right = len(list)-1
    while left <= right:
        middle = (left + right) // 2
        if list[middle] == target:
            return middle
        if list[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return -1

