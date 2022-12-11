import libnum


def run():
  print("\n### solution to question [3] ###")

  a = 3  # given a
  b = 3  # given b
  p = 5  # prime number
  n = 50  # number of points to show
  x = 3  # x for starting point
  y = 2  # y for starting point

  result = []

  if ((y**2 % p) == ((x**3 + a * x + b) % p)):
    result.append([x, y])

  S = ((3 * x**2) + a) * pow(2 * y, -1, p)

  x1 = (S**2 - 2 * x) % p
  y1 = ((S * (x - x1)) - y) % p

  x3 = x1
  y3 = y1

  x2 = 0
  y2 = 0

  counter = 1

  result.append([x1, y1])
  for i in range(2, n + 1):
    counter = counter + 1
    if ((y1**2 % p) == ((x1**3 + a * x1 + b) % p)):
      result.append([x1, y1])

    try:
      rtn = pow(x1 - x, -1, p)
      if (rtn == 0):
        counter = counter + 2

        s = ((3 * x**2) + a) * pow(2 * y, -1, p)
        x1 = (s**2 - 2 * x) % p
        y1 = ((s * (x - x1)) - y) % p

        if ((y**2 % p) == ((x**3 + a * x + b) % p)):
          result.append([x1, y1])

      else:
        s = (y1 - y) * rtn
        x2 = (s**2 - x1 - x) % p
        y2 = ((s * (x1 - x2) - y1)) % p

        x1 = x2
        y1 = y2
        # result.append([x1, y1])

    except ValueError:
      break
  print("Result: ", result)

  #Given Q = [3, 3]
  Q = [3, 3]
  idx = 0
  for x in result:
    if x[0] == Q[0] and x[1] == Q[1]:
      idx = result.index(x) + 1
  print("Index of Q = ", idx)
