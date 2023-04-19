### Teacher Joel Peltonen
### 19.04.2023
### Py Intro day 3


price = 254
print(price)
print(hex(price))

print('----------')
print(hex(0))
print(hex(1))
print(hex(2))
print(hex(3))
print(hex(4))

print(hex(9))
print(hex(10))
print(hex(11))

print('----------')
red = 0xAA
print(red)

print('----------')
print(bin(1))
print(bin(2))
print(bin(3))
print(bin(4))
print(bin(5))
# print(bin(5.1)) Type error! This gets complex and Py won't show


print('----------')
mask1 = 0b1000
mask2 = 0b1011
print(mask1)
print(mask2)
print(bin(mask1 & mask2)) # Binary AND operator
print(bin(mask1 | mask2)) # Binary OR operator
print(bin(mask1 ^ mask2)) # Binary XOR operator
