# TASK-1

for x in range(1,11):
    print(x)


# TASK-2

num = int(input("Enter a number "))
total = 0
for x in range(1,num+1):
    total+=x
print(total)

# TASK-3

var = int(input("Enter a number "))
for x in range(1,11):
    print(f"{var} x {x} = {var*x}")


# TASK-4

numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i % 5 == 0:
        if i > 150:
            continue
        if i > 500:
            break
        print(i)


# TASK-5

a = [1,2,3,4,5]
for i in a[::-1]:
    print(i)


# TASK-6

start = 2
end = 14

for i in range(start, end):
    prime_flag = True
    for j in range(2, i):
        if i % j == 0:
            prime_flag = False
    if prime_flag == True:
        print(i)

# TASK-7

num = int(input("Enter a number "))
factorial = 1
for x in range(1,num+1):
    factorial*=x
print(factorial)


# TASK-8

num = int(input("Enter a number "))
thesum = 0
for i in range(1,  num+1):
    thesum += i
print(thesum)

# TASK-9

import random
ran_num = random.randint(1,9)

while True:
    inp = int(input("Guess a number! "))
    if inp == ran_num:
        print("Well guessed", ran_num)
        break
    else:
        inp = int(input("Try again "))

# TASK-10

word = str(input("Enter a word "))
reverse = word[::-1]
print(reverse)


# TASK-11

inp = str(input("Enter the word "))
letters = []
digits = []

for x in inp:
    if x.isalpha():
        letters.append(x)
    else:
        digits.append(x)
        
print(f"letters={letters}, digits={digits}") 


# TASK-12

inp = input("Enter the word ")
count = 0
for x in inp:
    count += 1

print("Word count: ",count)

# TASK-13
name = input("Enter name ")
vowels = []
consonants = []
for x in name:
    if x.lower() in 'aeiou':
        vowels.append(x)
    elif x.isalpha():
        consonants.append(x)

print(f"vowels={len(vowels)} and consonants={len(consonants)}")
    

# TASK-14

num_inp = int(input("Number of values? "))
value_list = []
for x in range(1,num_inp+1):
    value = input("Enter a value ")
    value_list.append(value)

print(value_list)


# TASK-15

list1 = ["python","java","c++","javascript","swift"]
list2 = []
for x in list1:
    list2.append(x)

print(list2)


# TASK-16

lst_num = [11,25,2,6,63,45]
lst_num.sort()
lst_num.reverse()
print(lst_num[0])


# TASK-17

numbers = [1,2,3,4,5,6,7,8,9]
even = []
odd = []
for x in numbers:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

print("Even: ", len(even), "Odd: ", len(odd))


# TASK-18

numbers = [3,5,23,6,5,1,2,9,8]
summ = 0
for x in numbers:
    summ += (x**2)

print(summ)


# TASK-19

gadgets = ["Mobile", "Laptop", 100, "Camera", 310.28, "Speakers", 
27.00, "Television", 1000, "Laptop Case", "Camera Lens"]

strings = []
digits = []

for x in gadgets:
    if type(x) == str:
        strings.append(x)
    else:
        digits.append(x)
        
digits.sort()
digits_reverse = digits.copy()
digits_reverse.reverse()
strings.sort()
strings_reverse = strings.copy()
strings_reverse.reverse()
