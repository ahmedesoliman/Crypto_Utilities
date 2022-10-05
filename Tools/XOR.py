C1 = 0x6ecb4d77f9a954ab
C2 = 0xbbf94552a33b55e7

temp = C1 ^ C2 #performing XOR operations

M1 = 0x23da91adcdb4e27c

M2 = temp ^ M1

cipherText = C1 ^ M1

print(hex(M2))
print(hex(cipherText))


a = "00000001000000000000001000000000"
b = "10001001111101001011101110100100"
c = "10001001111101001011000110100100"


y=int(a,2) ^ int(b,2)

print('{0:b}'.format(y))