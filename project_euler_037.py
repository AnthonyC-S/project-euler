


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


first_dig = [2,3,5,7]
middle_digs = [1,3,7,9]
last_dig = [3,7]

candidate_list = []

def generateNums(num_middle_digits, candidate_list):
  if num_middle_digits == 0:
    print("candidate_list: ", candidate_list)
    return candidate_list
  else:
    new_candidate_list = []
    for c in candidate_list:
      print("c: ", c)
      for m in middle_digs:
        print("m: ", m)
        new_candidate_list.append(c*10 + m)
        print("new_candidate_list: ", new_candidate_list)
    num_middle_digits = num_middle_digits - 1
    generateNums(num_middle_digits, new_candidate_list)

print("answer: ", generateNums(1, first_dig))