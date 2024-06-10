# Project Euler
# Problem 033

# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in 
# attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is 
# correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less than
# one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, find
# the value of the denominator.


def digitCancel():
  nums = [item for item in range(11, 99)]
  dens = [item for item in range(12, 100)]
  soln_nums = []
  soln_dens = []

  for i, num in enumerate(nums):
    for den in dens[i:]:
      val = num / den
      if (num % 10 != 0 and den % 10 != 0):
        if (num % 10 == den % 10 and (num // 10) / (den // 10) == val) or \
           (num % 10 == den // 10 and (num // 10) / (den % 10) == val) or \
           (num // 10 == den % 10 and (num % 10) / (den // 10) == val) or \
           (num // 10 == den // 10 and (num % 10) / (den % 10) == val):
          soln_nums.append(num)
          soln_dens.append(den)
  
  soln_num_prod = 1
  soln_den_prod = 1

  for i in range(len(soln_nums)):
    soln_num_prod *= soln_nums[i]
    soln_den_prod *= soln_dens[i]
  
  return int(soln_den_prod / soln_num_prod)

print(digitCancel())