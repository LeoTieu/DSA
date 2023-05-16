def binary_search(list, target):
    '''
    Searches a target and returns target's index.
    Returns -1 if target was not found.
    Time complexity is O(log n) where n is the list length.
    '''
    left = 0
    right = len(list) - 1
    while left <= right:
        middle = (left + right) // 2
        if list[middle] > target:
            right = middle - 1
        elif list[middle] < target:
            left = middle + 1
        else:
            return middle
    return -1

