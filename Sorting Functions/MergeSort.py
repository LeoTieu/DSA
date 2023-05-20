# Personal comments:
# hmu if I do something "wrong"
# or if u have any feedback

# For the Merge function. Why append pointers instead of pop?
# Shifting elements take o(n)
# Emptying the whole list will be quadratic in time. >

def merge_sort(List):
    '''Merge sort function.'''
    if len(List) > 1:
        # Get middle index
        split_index = len(List) // 2

        # Left list
        Left_List = List[:split_index]

        # Right list
        Right_List = List[split_index:]
        
        # Sort left list
        Left_List = merge_sort(Left_List)

        # Sort right list
        Right_List = merge_sort(Right_List)

        # Sort left + right list
        List = []
        pointer_1 = 0
        pointer_2 = 0
        while pointer_1 < len(Left_List) and pointer_2 < len(Right_List):
            # Checks which element is bigger
            if Left_List[pointer_1] <= Right_List[pointer_2]:
                # Adds element and moves pointer
                List.append(Left_List[pointer_1])
                pointer_1 += 1
            else:
                List.append(Right_List[pointer_2])
                pointer_2 += 1
        # if pointer_1 outside l1. Add the rest of l2.
        # And vice versa ofc.
        if pointer_1 == len(Left_List):
            List += Right_List[pointer_2:]
        else:
            List += Left_List[pointer_1:]
        return List            
    else:
        return List


if __name__ == '__main__':
    arr = [3, 20, 7, 9, 13, 14, 10, 2, 5, 1, 8, 18, 4, 11, 15, 6, 16, 19, 12, 17]
    print(merge_sort(arr))

