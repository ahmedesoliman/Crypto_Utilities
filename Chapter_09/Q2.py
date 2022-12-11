# @file: Q2.py
# chapter_09 CSCI 360 Cryptography & crypto analysis
# @author: ahmedesoliman
# @breif: solutions to webwork crypto homework chapter 9
# @version: 0.1
# @date: 12-3-2022
# @copyright: copyright (c) 2022
import sys
import libnum


def run():
  print("\n### solution to question [2] ###")

  a = 3  # given a
  b = 14  # given b
  p = 17  # prime number
  n = 50  # number of points to show
  x = 1  # x for starting point
  y = 1  # y for starting point

  z = (x**3 + a * x + b) % p
  if (libnum.has_sqrtmod(z, {p: 1})):
    y = next(libnum.sqrtmod(z, {p: 1}))

  print("P\t(%d,%d)" % (x, y), end=' ')

  if ((y**2 % p) == ((x**3 + a * x + b) % p)): print("  \tPoint is on curve")
  else:
    print("  \tPoint is not on curve")
    sys.exit()

  s = ((3 * x**2) + a) * libnum.invmod(2 * y, p)

  x1 = (s**2 - 2 * x) % p

  y1 = ((s * (x - x1)) - y) % p

  x3 = x1
  y3 = y1
  x2 = 0
  y2 = 0
  counter = 1

  for i in range(2, n + 1):
    counter = counter + 1
    if (counter > n): sys.exit()

    print("%dP\t(%d,%d)" % (counter, x1, y1), end=' ')
    if ((y1**2 % p) == ((x1**3 + a * x1 + b) % p)):
      print("  \tPoint is on curve")

    try:
      rtn = pow(x1 - x, -1, p)
      if (rtn == 0):
        print("%dP=0" % (counter + 1))
        counter = counter + 2
        s = ((3 * x**2) + a) * libnum.invmod(2 * y, p)

        x1 = (s**2 - 2 * x) % p
        y1 = ((s * (x - x1)) - y) % p

        print("%dP\t(%d,%d)" % (counter, x, y), end=' ')
        if ((y**2 % p) == ((x**3 + a * x + b) % p)):
          print("  \tPoint is on curve")

      else:
        s = (y1 - y) * rtn

        x2 = (s**2 - x1 - x) % p

        y2 = ((s * (x1 - x2) - y1)) % p

        x1 = x2
        y1 = y2
    except ValueError:
      break

  print("Cardinality counter = ", counter + 1)
