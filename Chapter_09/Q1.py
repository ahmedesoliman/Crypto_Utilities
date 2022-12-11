# @file: Q1.py
# chapter_09 CSCI 360 Cryptography & crypto analysis
# @author: ahmedesoliman
# @breif: solutions to webwork crypto homework chapter 9
# @version: 0.1
# @date: 12-3-2022
# @copyright: copyright (c) 2022

a = 2
b = 1
p = 5


## find slope of an eliptic curve given P & Q
def checkPQ(x1, y1, x2, y2):
  if (x1 == x2) and (y1 == y2):
    algo2(x1, y1, x2, y2)
  elif (x1 == x2) and (y1 != y2):
    algo1(x1, y1, x2, y2)
  else:
    algo1(x1, y1, x2, y2)


# if P != Q use algo 2
def algo1(x1, y1, x2, y2):
  S = (y2 - y1) // (x2 - x1) % p
  x3 = (S**2 - x1 - x2) % p
  y3 = (S * (x1 - x3) - y1) % p
  print("(xy) = (", x3, ",", y3, ")")


# if P == Q use algo 2
def algo2(x1, y1, x2, y2):
  S = (3 * (x1**2) + a) / (2 * y1) % p
  x3 = (S**2 - x1 - x2) % p
  y3 = (S * (x1 - x3) - y1) % p
  print("(xy) = (", x3, ",", y3, ")")


def run():
  print("\n### solution to question [1] ###")

  # Change for box 1
  point_P = [0, 1]
  point_Q = [0, 1]

  #Don't change
  x1 = point_P[0]
  y1 = point_P[1]
  x2 = point_Q[0]
  y2 = point_Q[1]
  checkPQ(x1, y1, x2, y2)

  #change for box 2
  point1 = [0, 4]
  point2 = [1, 2]

  #Don't change
  a = point1[0]
  b = point1[1]
  c = point2[0]
  d = point2[1]
  checkPQ(a, b, c, d)

  # change values to values in box 3
  Z = 5
  x1 = 1
  y1 = 3
  print("Inverse = (", x1, ",", pow(y1, -1, Z), ")")
