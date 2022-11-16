n = 2395641605

factors = []
while n % 2 == 0: 
    factors += [2]
    n //= 2
        
# n must be odd at this point
for i in range(3, int(n**0.5) + 1, 2): 
        
    # while i divides n
    while n % i == 0: 
        factors += [i]
        n //= i 
            
if n > 2: 
    factors += [n]

dict = {}
for p in factors:
    if p in dict:
        dict[p] += 1
    else:
        dict[p] = 1
    
primes = list(dict.keys())
exponents = list(dict.values())

phiOfn = 1
for i in range(len(primes)):
    phiOfn *= (primes[i]**exponents[i] - primes[i]**(exponents[i]-1))

# Print the output
print("Primes = ", primes)
print("Expo = ", exponents)
print("Phi(n) = ", phiOfn)