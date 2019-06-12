#Exercise 1

values = set()

def is_whole(n):
  return n % 1 == 0

while True:
  number = input("Enter a number: ")
  if is_whole(number):
    values.add(number)
    print repr(number) + " - result: " + str(len(values))