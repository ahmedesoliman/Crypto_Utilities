# @file: Q4.py
# chapter_09 CSCI 360 Cryptography & crypto analysis
# @author: ahmedesoliman
# @breif: solutions to webwork crypto homework chapter 9
# @version: 0.1
# @date: 12-3-2022
# @copyright: copyright (c) 2022

P = [1, 1]
p = 17
a = 3
b = 14

n = 51 #arbitrary rounds change to large number better


def gcdExtended(a, b):
  if a == 0:
    return b, 0, 1
  gcd, x1, y1 = gcdExtended(b % a, a)
  x = y1 - (b // a) * x1
  y = x1
  return gcd, x, y


def double_point(point: list):
  x = point[0]
  y = point[1]

  s = ((3 * (x**2) + a) * (gcdExtended(2 * y, p)[1])) % p

  newx = (s**2 - x - x) % p
  newy = (s * (x - newx) - y) % p

  return [newx, newy]


def add_points(P: list, Q: list):
  x1 = P[0]
  y1 = P[1]
  x2 = Q[0]
  y2 = Q[1]

  #s = ((y2 - y1) * ((gcdExtended(x2-x1, prime))[1] % prime)) % prime
  s = (y2 - y1) * (gcdExtended(x2 - x1, p)[1] % p)

  newx = (s**2 - x1 - x2) % p
  newy = (s * (x1 - newx) - y1) % p

  return [newx, newy]


def run():
  print("\n### solution to question [4] ###")
  Q = P
  index = 2
  while True:
    if Q[0] == P[0] and Q[1] == P[1]:
      # print("doubling")
      Q = double_point(P)
    else:
      # print("adding")
      Q = add_points(P, Q)

    if index == n:
      break

    print(f"{index}P = {Q}")
    index += 1
