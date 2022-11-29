# Author: ahmedesoliman
# Breif: crack deffie-hellman key exchange algo using DLP 
# Assume public keys are given as well as the premitive element and the base alpha are given

A = 61     # Chnage to A
B = 49     # Change to B
p = 97     # change mod here
alpha = 5  # change base here

a_prv = 0
b_prv = 0

for x in range(0, p):
    calc = alpha ** x % p
    if calc == A:
      a_prv = x
      print("Private key for A: ", x)
    if calc == B:
        b_prv = x
        print("Private key for B: ", x)
    # print('%s^%s ≡ %s mod %s' % (alpha, x, calc, p))
      
print("Shared secret: ", A ** b_prv % p)
print("Shared secret: ", B ** a_prv % p)