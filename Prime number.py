def find_primes(n):
    primes = []
    for num in range(2, n+1):
        is_prime = True
        for i in range(2, int(num**(1/2))+1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

n = int(input("enter a number: "))
primes = find_primes(n)
print(primes)