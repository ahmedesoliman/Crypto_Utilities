def main():
  
  n = 437

  fl = []
  
  for a in range(2, n-1):
    if((a**(n-1) % n) == 1):
      fl.append(a)
      
  print(fl)

main()

