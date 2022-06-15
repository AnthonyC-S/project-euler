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