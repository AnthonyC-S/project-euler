# The number, 197, is called a circular prime because all rotations of the 
# digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 
# 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?

import math

circ_primes = {2,3,5,7}


def isPrime(n):
  for i in range(2, math.ceil(math.sqrt(n))+1):
    if n % i == 0:
      return False
  return True

def performShifts(n):
  if n in circ_primes:
    return
  num_shifts = math.floor(math.log10(n))
  num_digits = num_shifts + 1
  for i in range(0, num_digits):
    dig = n % 10**(i+1) // 10**i
    if dig == 0 or dig == 2 or dig == 4 or dig == 5 or dig == 6 or dig == 8:
      return

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
  n = 11
  while n < 1000000:
      performShifts(n)
      n += 2
  
  return len(circ_primes)

print(circularPrime())