#factorial
def fac(n):
  if n <= 1:
    return 1
  else:
    return n * fac(n-1)

#fabonacci
def fabonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fabonacci(n-1) + fabonacci(n-2)

#SUM of DIGITS

def sum_digits(n):
  if n < 10:
    return n
  else:
    return n % 10 + sum_digits(n // 10)


#Sum of List

def sum_list(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])


# Power
def power(base, exponent):
  if exponent == 0:
    return 0
  elif exponent == 1:
    return base
  else:
    return base * power(base, exponent-1)


#square
def square_list():
  sqr = []
  for j in range(2,30):
    sqr.append(j+j)
  return sqr

def checkNum (num, start, end) :
  if num in range(start,end):
    return "Number in range"
  else:
     return "Not in range"

def checkText(text):
  upperLetter = 0
  lowerLetter = 0
  for x in text:
    if x.isupper():
      upperLetter += 1
    elif x.islower():
      lowerLetter += 1
  return ("Upper:",upperLetter, lowerLetter)

def is_palindrome(s):
  s = s.lower().replace("","")
  return s == s[::-1]
