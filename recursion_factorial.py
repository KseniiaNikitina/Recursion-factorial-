def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


number = 8
result = factorial(number)
print(f" {number}! = {result}")