# python program to print prime factors
 
import math

result = []
def primefactors(n):
   #even number divisible
   while n % 2 == 0:
      print (2),
      n = n / 2
    
   #n became odd
   for i in range(3,int(math.sqrt(n))+1,2):
     
      while (n % i == 0):
        print (i)
        result.append(i)
        n = n / i
    
   if n > 2:
      print (n)

 
n = 1139 
primefactors(n)

lst = [*set(result)]

print(lst)







