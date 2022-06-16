# Project Euler - Problem 36
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic 
# in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include 
# leading zeros.)
#
# Note, a faster method would be to generate the palindromes in one base first 
# and then check the other base.

import time

start_time = time.time()

def isPalindrome(n):
  temp_num = n
  rev_num = 0
  while (temp_num):
    rev_num = rev_num * 10 + temp_num % 10
    temp_num //= 10
  return n == rev_num

sum = 0
n = 1
while n < 1000000:
  if isPalindrome(n) and isPalindrome(int(bin(n)[2:])):
    sum += n
  n += 2

print(sum)
print("--- %s seconds ---" % (time.time() - start_time))