def calculator():
  num1 = float(input("Enter 1st number "))
  num2 = float(input("Enter 2nd number "))

  sum_result = num1 + num2
  print("sum", sum_result)

  difference = num1 - num2
  print("difference", difference)

  multiply = num1 * num2
  print("multiple", multiply)

  if num2 == 0:
    print("Denominator can't be 0")
  else:
    division = num1 / num2
    print("Division", division)




def is_palindrome(s):
  s = s.lower().replace("","")
  return s == s[::-1]

word = input("Enter a word ")
if is_palindrome(word):
  print("it is a palindrome word")
else:
  print("it is not a palindrome")

def dolist(li):
  sum = 0
  for x in li:
    sum += x
  print ("Sum:",sum)
  li.sort()
  print("Sorted",li)
  print("Minimum", li[0])
  li.reverse()
  print("Maximum", li[0])
