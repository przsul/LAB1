# Exercise 2

binary = raw_input("Enter binary string: ")
ones = binary.count('1')
tmp = 0

i = 0
while i < len(binary):
  if i == len(binary)-1:
    i += 1
    continue
  if binary[i] == '1' and binary[i+1] == '1':
    tmp += 1
  i += 1

print "Number of gaps: " + str(ones-1-tmp)