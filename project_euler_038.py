# Pandigital Mltiples
# Problem 38

# Take the number 192 and multiply it by each of 1, 2, and 3:

# 192 x 1 = 192
# 192 x 2 = 384
# 192 x 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will 
# call 192384576 the concatenated product of 192 and (1,2,3)

# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, 
# and 5, giving the pandigital, 918273645, which is the concatenated product 
# of 9 and (1,2,3,4,5).

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
# concatenated product of an integer with (1,2, ... , n) where n > 1?

from itertools import permutations
from math import floor,log10


# Length Calculator
def n_len(n):
    digits = floor(log10(n)) + 1
    return digits 

def isPandigital(n):
  num_digits = 0
  while num_digits < 10:
    for i in range(1,5):
      n1 = n // 10**(9 - i)
      n2 = n1*2
      n3 = n1*3
      n4 = n1*4
      n5 = n1*5
      print(n)
      print(n1, n2, n3, n4, n5)
      print()

      

  # for i in range(1,5)   this will check the integers 9, 98, 987, 9876 for n = 1


isPandigital(918273645)

l = list(permutations(range(9,0,-1)))
possible_results = []

for i in range(40320):
  combined_number = 0
  for i, n in enumerate(l[i]):
    combined_number += n * 10**(8-i)
  possible_results.append(combined_number)


