# The number, 197, is called a circular prime because all rotations of the 
# digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 
# 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?

import math

circ_primes = set()

def isPrime(n):
  if n == 2:
    return True

  for i in range(2, math.ceil(math.sqrt(n))):
    if n % i == 0:
      return False
    else:
      return True

def performShifts(n):
  if n in circ_primes:
    return
  num_shifts = math.floor(math.log10(n))
  shift_pos = 10**num_shifts
  temp_circ_primes = []
  while (num_shifts > -1):
    if not isPrime(n):
      return
    else:
      temp_circ_primes.append(n)
      n = n % shift_pos * 10 + n // shift_pos
      num_shifts -= 1
  circ_primes.update(temp_circ_primes)
    
def circularPrime():
  n = 2
  while n < 100:
    if n < 10 and isPrime(n):
      circ_primes.add(n)
      n -= 1
    else:
      performShifts(n)
      n -= 1
  
  return len(circ_primes)


print(circularPrime())