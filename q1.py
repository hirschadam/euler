
def multiples(n, a, b):
    total = 0
    i = 0
    while(i < n):
        if(i % a == 0):
            total += i
        elif (i % b == 0):
            total += i
        i += 1
    return total

def multiples2():
    for number in range(1000):
        if not number % 3 or not number % 5:
            yield number
def main():
    #my solution
    print (multiples(1000,3,5))
    #solution using a generator
    print (sum(multiples2()))

main()