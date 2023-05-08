n1 = 23477
n2 = 31213

print(bin(n1)[2:])  # 101101110110101
print(bin(n2)[2:])  # 111100111101101

# AND, 1 AND 1 = 1
n3 = n1 & n2
print(bin(n3)[2:])      # 101100110100101


# OR, 0 OR 0 = 0
n4  = n1 | n2
print(bin(n4)[2:])      # 111101111111101


# XOR, 1 XOR 0 = 1,  0 XOR 1 = 1
n5 = n1 ^ n2
print("0" + bin(n5)[2:])        # 010001001011000


# NOT, ~ only works on signed integers
print("0" + bin(0b111111111111111 - n1)[2:])        # 010010001001010


# SHIFTS, shifts binary number to the left or to the right.
number = 20
number <<= 1
print(bin(number))      # 0b101000

number >>= 2
print(bin(number))      # 0b1010
