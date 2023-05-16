# Personal comments:
# hmu if I do something "wrong"

# Why not pop(0)?
# Shifting elements take o(n)
# Emptying the whole list will be quadratic in time.

def Merge(l1,l2):
    '''Merges 2 sorted lists'''
    # Result list. Will be returned.
    l3 = []
    # Points to the first element of list.
    pointer_1 = 0
    pointer_2 = 0 
    while pointer_1 < len(l1) and pointer_2 < len(l2):
        # Checks which element is smallest.
        if l1[pointer_1] <= l2[pointer_2]:
            # Adds element where pointer is located at.
            l3.append(l1[pointer_1])
            # Points to next element.
            pointer_1 += 1
        else:
            l3.append(l2[pointer_2])
            pointer_2 += 1
    # if pointer_1 outside l1. Add the rest of l2.
    # And vice versa ofc.
    if pointer_1 == len(l1):
        l3 += l2[pointer_2:]
    else:
        l3 += l1[pointer_1:]
    return l3

