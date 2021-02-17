import math

def primes(n):
    composites = []
    prime = [2]
    i = 3

    while (i <= n):
        if i not in composites:
            prime.append(i)
            j = i
            while (j <= ( n / i )):
                composites.append(i*j)
                j += 1
        i += 2

    return prime

def eratosthenes(n):
    req_prime = primes(int(math.sqrt(n)))
    result = [2]
    i = 3
    sum = 2
    if n == 1:
        return []
    while (i <= n):
        for prime in req_prime:
            if i != prime and i % prime == 0:
                break
        else:
            result.append(i)
            sum += i
        i = i + 2

    return sum #,result

def prime_factorize(num):
    pos_prime = eratosthenes(int(math.sqrt(num)))

    for divisor in pos_prime:
        if num % divisor == 0:
            temp = int(num / divisor)
            return str(divisor) + ', ' + str(prime_factorize(temp))
    return str(num)

print(eratosthenes(2000000))