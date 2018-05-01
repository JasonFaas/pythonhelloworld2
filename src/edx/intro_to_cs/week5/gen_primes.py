def isPrime(prime_value, all_primes):
    for prev_prime in all_primes:
        if prime_value % prev_prime == 0:
            return False
    return True


def genPrimess():
    if False:
        yield False
    return True

def genPrimes():
    prime_value = 2
    all_primes = []
    while(True):
        if isPrime(prime_value, all_primes):
            all_primes.append(prime_value)
            yield prime_value
        prime_value += 1

print(genPrimess())

primes = genPrimes()
print(primes.__next__())
print(primes.__next__())
print(primes.__next__())
print(primes.__next__())
