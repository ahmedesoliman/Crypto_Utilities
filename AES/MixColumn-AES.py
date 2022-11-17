

valsList = [] # List of values

def mixColumns(val1, val2, val3, val4): # MixColumns
    print("Hex: ") # Print Hex
    printHex(gmul(val1, 2) ^ gmul(val2, 3) ^ gmul(val3, 1) ^ gmul(val4, 1)) 
    printHex(gmul(val1, 1) ^ gmul(val2, 2) ^ gmul(val3, 3) ^ gmul(val4, 1)) 
    printHex(gmul(val1, 1) ^ gmul(val2, 1) ^ gmul(val3, 2) ^ gmul(val4, 3))
    printHex(gmul(val1, 3) ^ gmul(val2, 1) ^ gmul(val3, 1) ^ gmul(val4, 2))
    

  
def gmul(a, b): # Galois Field (256) Multiplication of two Bytes
    if b == 1: # If b is 1, return a
        return a
    tmp = (a << 1) & 0xff # Shift a left by 1
    if b == 2: # If b is 2, return tmp
        return tmp if a < 128 else tmp ^ 0x1b # If a is less than 128, return tmp, else return tmp ^ 0x1b
    if b == 3: # If b is 3, return tmp ^ a
        return gmul(a, 2) ^ a # Return gmul(a, 2) ^ a

def printHex(val): 
    valsList.append(val) # Append val to valsList
    return print('{:02x}'.format(val), end=' ') # Print val in hex

# plug in hex values from question
mixColumns(0x64, 0xc8, 0x96, 0xfa) # 0x19 0x85 0x91 0x02 = 35 a2 a3 3b

print("\n")
for i in range(len(valsList)): # For i in range of valsList
  print("C", i ,"=", valsList[i]); # Print C, i, =, valsList[i]