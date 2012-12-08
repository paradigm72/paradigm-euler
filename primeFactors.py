import math

def primeFactors(n):
    listSize = int(math.sqrt(n)) + 1
    nonPrimes = [0] * listSize
    i = 2

    while (i * i < n):
        # if i is a known non-prime, nothing to do
        if nonPrimes[i] == 1:
           pass

        # otherwise, i is a prime
        else:
            if (n % i == 0):
                # i is a prime factor, so mark all its multiples as ineligible (not prime)
                j = i
                while (j * j < n):
                    nonPrimes[j] = 1
                    j += i

                print i
        i += 1

primeFactors(600851475143)
