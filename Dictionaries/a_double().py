# Implement a function that doubles all integers in a dictionary
# Comment: Use comprehension when learnt

def double(d):
    '''Doubles all integers in a dictionary'''
    for key in d:
        if type(d[key]) != int:
            continue
        d[key] = d[key] * 2
    return d

dict = {'1': 5,
        '2': 10,
        '3': 15,
        '4': 20,
        '5': '25'}


print(double(dict))