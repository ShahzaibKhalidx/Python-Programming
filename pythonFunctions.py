# TASK-1

def maxNum( a,b,c):
  if a > b and a > c:
    return a
  elif b > a and b > c:
    return b
  else:
    return c


# TASK-2

def mysum(mylist) :
  suum = 0
  for x in mylist :
    suum += x
  return suum

mylist = [5,9,3,5,4]
print(mysum(mylist))


# TASK-3
def factorial(num):
  myfactorial = 0
  if num < 0 :
    print("Num is negative!")
  else:
    myfactorial *= num
  return myfactorial

num = 5
print(factorial(num))


#4.Write a Python function to check whether a number falls within a given range.

def checkNum (num, start, end) :
  if num in range(start,end):
    return "Number in Range"
  else:
    return "Not in Range"


#5 Write a Python function that accepts a string and counts the number of upper- and lower-case letters.

def checkText(text):
  upperLetter = 0
  lowerLetter = 0
  for x in text:
    if x.upper() in text:
      upperLetter += 1
    elif x.lower() in text:
      lowerLetter += 1
  return (upperLetter, lowerLetter)


text = 'ShahZaiB'
print(checkText(text))


#6.Write a Python function that takes a list and returns a new list with distinct elements from the first list.


def distinct(lst) :
  return list(set(lst))


#7.

def is_prime(n):
  if n < 1:
    return False
  for i in range(2,n):
    if n % i == 0:
      return False
  return True


#8.Write a Python program to print the even numbers from a given list.

def even(lst):
  even_numbers = []
  for i in lst:
    if i % 2 == 0:
      even_numbers.append(i)
  print("Even",even_numbers)


#9.Write a Python function that checks whether a passed string is a palindrome or not.

def is_palindrome(s):
  s = s.lower().replace("","")
  return s == s[::-1]


#10.Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30

def square_list():
  sqr = []
  for j in range(1,30):
    sqr.append(j*j)
  return sqr