def SelectionSort(input_list):
    '''
    Sorts a list in quadtratic time O(N^2).
    '''
    for idx in range(len(input_list)):
        for comp_idx in range(len(input_list)):
            if input_list[idx] < input_list[comp_idx]:
                input_list[idx], input_list[comp_idx] = input_list[comp_idx], input_list[idx]
    return input_list

def SelectionSort2(input_list):
    '''
    Sorts a list in quadtratic time O(N^2).
    Imo, a bit more beginner friendly than first implementation. 
    Might not be a 'selection sort' sorting algorithm.
    '''
    sorted_list = []
    while len(input_list) > 0:
        smallest_number = input_list[0]
        for val in input_list:
            if val < smallest_number:
                smallest_number = val
        while smallest_number in input_list:
            sorted_list.append(smallest_number)
            input_list.remove(smallest_number)
    return sorted_list

if __name__ == '__main__':
    MyList = [5,1,7,2,7,3,2,1,5]
    print(SelectionSort(MyList))
    print(SelectionSort2(MyList))
    # Both outputs are, [1, 1, 2, 2, 3, 5, 5, 7, 7]