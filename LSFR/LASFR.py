from pylfsr import LFSR


def checkIfequal(x, y):
  for k in range(4):
    if (x[k] == y[k]):
      return 1
  return 0


#for 5-bit LFSR with polynomial  x^4 + x^2 +1
state = [0, 1, 1, 0]
fpoly = [4, 2]
L = LFSR(initstate=state, fpoly=fpoly, counter_start_zero=False)
print('count \t state \t\toutbit \t seq')
print('-' * 50)

for i in range(15):
  print(L.count, L.state, '', L.outbit, L.seq, sep='\t')
  if (checkIfequal(L.state, state)):
    print("Period = ", L.count - 1)

  L.next()

print('-' * 50)
print('Output: ', L.seq)
