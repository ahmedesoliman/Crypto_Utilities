
# Python3 program to find a distinct
# prime number pair whose product
# is equal to given number
 
# from math lib. import everything
from math import *
 
# Function to generate all prime
# numbers less than n
def SieveOfEratosthenes(n, isPrime) :
 
    # Initialize all entries of boolean
    # array as true. A value in isPrime[i]
    # will finally be false if i is Not a
    # prime, else true bool isPrime[n+1];
    isPrime[0], isPrime[1] = False, False
 
    for i in range(2, n + 1) :
        isPrime[i] = True
 
    for p in range(2, int(sqrt(n)) + 1) :
 
        # If isPrime[p] is not changed,
        # then it is a prime
        if isPrime[p] == True :
 
            for i in range(p * 2, n + 1, p) :
                isPrime[i] = False
 
# Function to print a prime pair
# with given product
def findPrimePair(n) :
 
    flag = 0
     
    # Generating primes using Sieve
    isPrime = [False] * (n + 1)
    SieveOfEratosthenes(n, isPrime)
 
    # Traversing all numbers to
    # find first pair
    for i in range(2, n) :
        x = int(n / i)
 
        if (isPrime[i] & isPrime[x] and
             x != i and x * i == n) :
            print(i, x)
            flag = 1
            break
 
    if not flag :
        print("No such pair found")
     
# Driver code    
if __name__ == "__main__" :
 
    # Function calling
    n = 1139
 
    findPrimePair(n)
 