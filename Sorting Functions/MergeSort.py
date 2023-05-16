# Personal comments:
# Why not pop(0)?
# Shifting elements take o(n)
# Emptying the whole list will be quadratic in time.

def Merge(l1,l2):
    '''Merging 2 sorted lists'''
    l3 = []
    # Points to the first element of list
    pointer_1 = len(l1) * -1
    pointer_2 = len(l2) * -1
    while pointer_1 != 0 and pointer_2 != 0:
        if l1[pointer_1] <= l2[pointer_2]:
            l3.append(l1[pointer_1])
            pointer_1 += 1
        else:
            l3.append(l2[pointer_2])
            pointer_2 += 1
    if pointer_1 == 0:
        l3 += l2[pointer_2:]
    else:
        l3 += l1[pointer_1:]
    return l3
