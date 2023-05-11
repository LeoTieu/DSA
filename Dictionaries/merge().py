# Implement a function that merges 2 dictionaries

def merge_dict(dict1, dict2):
    '''Merges 2 dictionaries
    Ignores duplicates'''
    for key in dict1:
        dict2[key] = dict1[key]
    return dict2

if __name__ == '__main__':
    my_dict1 = {'banana': True,
            'apple': True,
            'pear': True}

    my_dict2 = {'grape': True,
                'pineapple': True,
                'apple': True}

    print(merge_dict(my_dict1,my_dict2))