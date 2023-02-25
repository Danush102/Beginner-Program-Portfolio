
#defining a function to find primes
def find_primes(n):
    #creating prime number list
    primes = []
    #searching for rime numbers
    for num in range(2, n+1):
        is_prime = True
        for i in range(2, int(num**(1/2))+1):
            if num % i == 0:
                is_prime = False
                break
                #adding the numbers found to the prime number list
        if is_prime:
            primes.append(num)
    return primes

#taking user input
n = int(input("enter a number: "))
#calling find primes function
primes = find_primes(n)
#printing output
print(primes)