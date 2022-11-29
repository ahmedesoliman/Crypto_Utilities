
def dlp(p, g, r):
  for i in range(p):
    if(g ** i) % p == r:
      return i

def main():
  p = 1879
  g = 3
  r = 9
  e = dlp(p, g, r)
  print ("Exponent: ", e)

main()