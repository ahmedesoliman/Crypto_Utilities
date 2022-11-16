# @Brief: A python program to compute the phi function value using eulerstotient algorithm
# @author: ahmedesoliman


def EulersTotient(N):

  # Setting initial number of totatives to N
  ans = N
  i = 2

  while (i * i <= N):

    if (N % i == 0):
      ans = (ans - int(ans / i))

    while (N % i == 0):
      N = N / i

    i += 1

  if (N > 1):
    ans = ans - int(ans / N)

  return str(int(ans))


def main():
  n = 1139
  print("Φ(n) = " + EulersTotient(n))


if __name__ == "__main__":
  main()
