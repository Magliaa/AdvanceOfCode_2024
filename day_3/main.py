import re


'''
  PART 1 & 2:
  Given a corrupted file, return a list of all the mul(num,num) that aren't ""after"" a don't() function.
'''
def get_expression(corrupted_file: str) -> list:
  expression_list: list = []
  pattern = r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)'
  expression_list = re.findall(pattern, corrupted_file)
  final_expression_list = []
  is_blocked = False

  for expression in expression_list:
    if expression == "do()":
      is_blocked = False
    elif expression == "don't()":
      is_blocked = True
    elif not is_blocked:
      final_expression_list.append(expression)
      
  final_expression_list = [re.findall(r'\d+', expression) for expression in final_expression_list]

  return final_expression_list


if __name__ == "__main__":    
  with open("input.txt", "r") as file:
    corrupted_file = file.read()

  expression_list = get_expression(corrupted_file)
  result: int = 0

  for expression in expression_list:
    result += int(expression[0]) * int(expression[1])

  print(result)

  
