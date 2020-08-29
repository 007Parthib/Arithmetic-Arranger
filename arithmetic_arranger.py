def arithmetic_arranger(problems, n = False):  
  if len(problems) > 5:
    return "Error: Too many problems."
  
  Line1 = ""
  Line2 = ""
  Line3 = ""
  Line4 = ""
  
  for i, problem in enumerate(problems):
    Number1, op, Number2 = problem.split()
  
    if not op in ["+","-"]:
      return "Error: Operator must be '+' or '-'."
  
    if not Number1.isdigit() or not Number2.isdigit():
      return "Error: Numbers must only contain digits."
  
    if len(Number1) > 4 or len(Number2) > 4:
      return "Error: Numbers cannot be more than four digits."
  
    if op == "+":
      solutions = int(Number1) + int(Number2)
  
    else:
      solutions = int(Number1) - int(Number2)
  
    num_length = len(max([Number1,Number2], key=len))
  
    Line1 += Number1.rjust(num_length+2)
    Line2 += op+Number2.rjust(num_length+1)
    Line3 += '-'*(num_length+2)
    Line4 += str(solutions).rjust(num_length+2)  
    
    if i < len(problems)-1:
      Line1 += "    "
      Line2 += "    "
      Line3 += "    "
      Line4 += "    "
  
    if n==True:
     arranged_problems = Line1 +"\n" + Line2 + "\n" + Line3 + "\n" + Line4
  
    else:
     arranged_problems = Line1 +"\n" + Line2 + "\n" + Line3

  '''if arranged_problems== "   32         1      45      123\n- 698    - 3801    + 43    +  49\n-----    ------    ----    -----\n -666     -3800      88      172":
      print("Success")   
  else:
     print("   32         1      45      123\n- 698    - 3801    + 43    +  49\n-----    ------    ----    -----\n -666     -3800      88      172")'''
  
  return arranged_problems
