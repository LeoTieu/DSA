a = 10      # 0b01010
b = 20      # 0b10100

a ^= b      # 0b11110
b ^= a      # 0b01010
a ^= b      # 0b10100

print(a) # 20
print(b) # 10