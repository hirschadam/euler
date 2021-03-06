# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

# Highly efficient fibonacci calculator
from math import sqrt
def F(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))


# Main implementation starts here
def F2():
    a,b = 0,1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b

count = 0
for index, fibonacci_number in enumerate(F2()):
    #do not exceed 4,000,000
    if fibonacci_number >= 4000000:
        break
    if not fibonacci_number % 2:
        count+= fibonacci_number

print('Sum of even fibonacci numbers: %d' % count)

