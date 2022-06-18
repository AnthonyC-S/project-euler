# Truncatable primes
# Problem 37
#
# The number 3797 has an interesting property. Being prime itself, it is 
# possible to continuously remove digits from left to right, and remain prime 
# at each stage: 3797, 797, 97, and 7. 
# Similarly we can work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to 
# right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.


import math


def isPrime(n):
  for i in range(2, math.ceil(math.sqrt(n))+1):
    if n % i == 0:
      return False
  return True


def getTruncPrimes():

  trunc_primes = []
  n = 11

  while len(trunc_primes) < 11:
    temp_n = n
    while(temp_n):
      

  n += 2 

  return sum(trunc_primes)

