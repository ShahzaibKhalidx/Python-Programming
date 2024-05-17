#TASK-1

user_marks = int(input("Enter the total marks obtained by student out of 1100..."))
user_percent = user_marks  / 1100 * 100
if 100 >= user_percent >= 90:
    print(f"With {user_marks} marks. You got \"A\" grade")
elif 90 >  user_percent >= 75:
    print(f"With {user_marks} marks. You got \"B\" grade")
elif  75 > user_percent >= 65:
    print(f"With {user_marks} marks. You got \"C\" grade")
elif  65 > user_percent > 33:
    print(f"With {user_marks} marks. You are pass!")
elif  user_percent < 33:
    print (f"With {user_marks} marks.You are fail!")
else:
    print("Please Enter valid marks")
        
# TASK-2

num = int(input("Enter a Number "))
if num < 0:
    print("It is a negative number")
else:
    print("It is a positive number")

#TASK-3

user_input = int(input("Enter a Number "))
if user_input % 2 == 0:
    print("Is it an Even number!")
else:
    print("It is an  Odd number")

# TASK-4

num = int(input("Enter the number "))
if num == 1:
    print("It is not a prime number")
elif num > 1:
    for x in range(2, num):
        if (num % x) == 0:
            print("It is not a Prime number")
            break
        else:
            print("It is a Prime Number")
            break
else:
    print("It is not a prime number")


# TASK-5

num = int(input("Enter the number "))
if (num % 7) == 0:
    print("Hello")
else:
    print("Not Divisible by 7")


# TASK-6

x = int(input("Enter value one "))
y = int(input("Enter value two "))
if x > y:
    print(y)
elif y > x:
    print(x)


# TASK-7

var = input("Enter a English character ")
vowels = ["a","e","i","o","u"]
if var in vowels:
    print("It is a vowel")
else:
    print("It is not a consonant")


# TASK-8

len_1 = int(input("Enter length of side one "))
len_2 = int(input("Enter length of side two "))
len_hypotenuse = int(input("Enter length of hypotenuse "))
if (len_1**2 + len_2**2) == len_hypotenuse**2:
    print("It is a Right Angle TRiangle")
else:
    print("Not a right angle triangle")


# TASK-9

a = int(input("Enter value of a "))
b = int(input("Enter value of b "))
c = int(input("Enter value of c "))
sq_root = (b**2 - 4*a*c)**(1/2)
root_1 = (- b - sq_root) / 2*a
root_2 = (- b + sq_root) / 2*a
print(root_1,root_2)
if root_1 > 0 and root_2 > 0:
    print(f"Answer {root_1} and {root_2}, Roots are Real")
else:
    pass


# TASK-10:

score = int(input("Enter the player score"))
if score > 30:
    print("Kamran Akmal")
elif 20< score < 30:
    print("Shoaib Akhtar")
elif 10< score < 20:
    print("Shahid Afridi")


# TASK-11

pwd = input("Enter the password ")
if 7 <= len(pwd) <= 15:
    if '@' in pwd or '$' in pwd:
        if '1' in pwd or '0' in pwd:
            print("Passord is okay")
        else:
            print("Add a numeric value")
    else:
        print("Add an  special character")
else:
    print(f"Length should be 7-15. Lenght is:{len(pwd)}")


# TASK-12

user_inp = input("Enter a character ")
ascii_code = ord(user_inp)
if 65 <= ascii_code <= 90:
    print("It is a upper case")
elif 97 <= ascii_code <= 122:
    print("It is a lower case")


# TASK-13

inp = input("Enter a character ")
if len(inp) > 1:
    print("enter single character only")
    
if len(inp) == 1:
    if inp.isalpha():
        print("it is a character")
    else:
        print("it is not a character")


# TASK-14

inp_1 = int(input("enter digit one of five "))
inp_2 = int(input("enter digit two of five "))
inp_3 = int(input("enter digit three of five "))
inp_4 = int(input("enter digit four of five "))
inp_5 = int(input("enter digit five of five "))
    
inp_list = [inp_1,inp_2,inp_3,inp_4,inp_5]
inp_set  = set(inp_list)

if len(inp_list) != len(inp_set):
    print("DUPLICATES")
else:
    print("ALL UNIQUE")


# TASK-15

user_value = int(input("Enter an integer value"))

if 1 < user_value < 101:
    print("OK")