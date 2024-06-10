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
import time

first_dig = [2,3,5,7]
middle_digs = [1,3,7,9]
last_dig = [3,7]

def generateNums(num_middle_digits, candidate_list):
  if num_middle_digits == 0:
    final_candidate_list = []
    for c in candidate_list:
      for d in last_dig:
        final_candidate_list.append(c*10 + d)
    return final_candidate_list

  else:
    new_candidate_list = []
    for c in candidate_list:
      for m in middle_digs:
        new_candidate_list.append(c*10 + m)
    num_middle_digits -= 1
    return generateNums(num_middle_digits, new_candidate_list)

def isPrime(n):
  if n == 1:
    return False
  if n == 2:
    return True
  for i in range(2, math.ceil(math.sqrt(n))+1):
    if n % i == 0:
      return False
  return True

def checkTruncations(trunc_list):
  for t in trunc_list:
    if not isPrime(t):
      return False
  return True

def getTruncations(n):
  trunc_list = []
  n_temp = n
  while n_temp != 0:
    trunc_list.append(n_temp)
    n_temp //= 10
  for i in range(1, len(trunc_list)):
    trunc_list.append(int(n % 10**i))
  return trunc_list

# Method 1: Generate list of plausible truncatable primes:
method1_start = time.time()
candidate_list = []
for i in range(5):
  candidate_list += generateNums(i, first_dig)

results = []

for c in candidate_list:
  if checkTruncations(getTruncations(c)):
    results.append(c)

print("Method 1")
print("Results: ", results)
print("Length of results: ", len(results))
print("Sum of results: ", sum(results))
method1_end = time.time()
print(method1_end - method1_start)

# Method 2: Iterate 10 through 740,000 and check each one
method2_start = time.time()
results = []

for c in range(11, 740000, 2):
  if checkTruncations(getTruncations(c)):
    results.append(c)

print("Method 2")
print("Results: ", results)
print("Length of results: ", len(results))
print("Sum of results: ", sum(results))
method2_end = time.time()
print(method2_end - method2_start)