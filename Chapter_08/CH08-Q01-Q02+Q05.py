def order(n):
  #assume that n is prime

  os = []  #possible orders

  for i in range(1, n):
    if (n - 1) % (i) == 0:
      os.append(i)

  # now I need to find elements with its order
  es = []

  for g in range(1, n):
    for i in os:
      if (g**i) % n == 1:
        es.append([g, i])
        break
  return os, es


def main():
  # change n to your value
  n = 1171
  os, es = order(n)
  pm = []

  print("\nPossible order: ", os)
  # print("\n Elements with its order: ", es)

  for i in range(len(es)):
    if (es[i][1] == n - 1):
      pm.append(es[i][0])

  print("Premitive: ", pm)  #question 5 
  print("Premitive elements #", len(pm))
  print("Probablity: ", len(pm) / n)
  # uncomment this for question 5
  # print(pm)


main()
