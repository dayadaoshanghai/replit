def factorial1(value):
    for i in range(1, value):
        value *= i
    return value



def factorial(value):
  if value == 1:
    return 1
  else:
    return value * factorial(value-1)

print(factorial(20))
print(factorial1(20))