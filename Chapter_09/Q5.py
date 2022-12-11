# @file: Q5.py
# chapter_09 CSCI 360 Cryptography & crypto analysis
# @author: ahmedesoliman
# @breif: solutions to webwork crypto homework chapter 9
# @version: 0.1
# @date: 12-3-2022
# @copyright: copyright (c) 2022

import math

a = 416
b = 547
p = 773


def run():
  print("\n### solution to question [5] ###")
  ans1 = int(p + 1 - 2 * math.sqrt(p))
  ans2 = int(p + 1 + 2 * math.sqrt(p))
  print("box1 = ", ans1)
  print("box2 = ", ans2)
