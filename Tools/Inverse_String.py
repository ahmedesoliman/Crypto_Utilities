
input = '0100101010101010101010101010'

output = ''

for i in range(0, len(input)):

  if (input[i] == '0'):
    output += '1'
  elif (input[i] == '1'):
    output += '0'

print(input);
print(output)