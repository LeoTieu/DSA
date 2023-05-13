# A set is a hashmap that stores key values.
# The difference between dictionary and a set is that
# Dictionary stores values with a key.

# Setting up an empty set
MySet = set()

# Setting up a set with values
MySet = {1,2,3,4}

# iterating through a set
for element in MySet:
    print(element)

# Adding to a set
MySet.add(5)

# Remove from a set
MySet.remove(5)

# Clear a set
MySet.clear()