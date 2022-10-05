valsList = []

def mixColumns(val1, val2, val3, val4):
    print("Hex: ")
    printHex(gmul(val1, 2) ^ gmul(val2, 3) ^ gmul(val3, 1) ^ gmul(val4, 1))
    printHex(gmul(val1, 1) ^ gmul(val2, 2) ^ gmul(val3, 3) ^ gmul(val4, 1))
    printHex(gmul(val1, 1) ^ gmul(val2, 1) ^ gmul(val3, 2) ^ gmul(val4, 3))
    printHex(gmul(val1, 3) ^ gmul(val2, 1) ^ gmul(val3, 1) ^ gmul(val4, 2))
    

  
def gmul(a, b):
    if b == 1:
        return a
    tmp = (a << 1) & 0xff
    if b == 2:
        return tmp if a < 128 else tmp ^ 0x1b
    if b == 3:
        return gmul(a, 2) ^ a

def printHex(val):
    valsList.append(val)
    return print('{:02x}'.format(val), end=' ')

# example from question
mixColumns(0x64, 0xc8, 0x96, 0xfa) # 0x19 0x85 0x91 0x02 = 35 a2 a3 3b

print("\n")
for i in range(len(valsList)):
  print("C", i ,"=", valsList[i]);