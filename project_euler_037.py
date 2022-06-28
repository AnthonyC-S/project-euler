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