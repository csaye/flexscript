def factorial(n):
    if n < 2:
        return n
    else:
        return n * factorial(n - 1)

n = 7
f = factorial(n)
print(f)
