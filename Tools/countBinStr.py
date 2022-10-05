# Order a binary string in new lines

binary = "0000000010100000000001000000100000010000000000000000000000000000"
count = "0"

for x in binary:
    count = int(count)
    count += 1
    count = str(count).zfill(2)
    print(count, "=", x)

initial_permutation = [(1, 58), (2, 50), (3, 42), (4, 34)]
