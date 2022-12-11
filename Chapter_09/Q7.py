# @file: Q7.py
# chapter_09 CSCI 360 Cryptography & crypto analysis
# @author: ahmedesoliman
# @breif: solutions to webwork crypto homework chapter 9
# @version: 0.1
# @date: 12-3-2022
# @copyright: copyright (c) 2022


def db_add(a, p, d, x, y):
  d = bin(d)
  x1 = x
  y1 = y
  P = []
  P.append([x1, y1])
  for i in range(3, len(d)):
    #double
    s0 = (2 * y1) % p
    s1 = pow(s0, -1, p)
    S = ((3 * x1**2 + a) * s1) % p

    x3 = ((S**2) - 2 * x1) % p
    y3 = (S * (x1 - x3) - y1) % p
    x1 = x3
    y1 = y3
    P.append([x1, y1])
    if (d[i:i + 1] == '1'):
      #add
      s0 = (x1 - x) % p
      s1 = pow(s0, -1, p)
      s = ((y1 - y) * s1) % p
      x3 = ((s**2) - x1 - x) % p
      y3 = (s * (x1 - x3) - y1) % p
      x1 = x3
      y1 = y3
      P.append([x1, y1])
  return P


def run():
  print("\n### solution to question [7] ###")
  a = 1798
  b = 2967
  p = 3079

  #Alice
  ad = 53
  x, y = 1, 1058
  P = db_add(a, p, ad, x, y)
  print(P[len(P) - 1])

  #bob
  bd = 25
  x, y = 1, 1058
  P = db_add(a, p, bd, x, y)
  print(P[len(P) - 1])

  #common key
  bd = 25  # keep as bob secret
  x, y = 1687, 593  # alice result
  P = db_add(a, p, bd, x, y)
  print("Ans =", P[len(P) - 1][0])
