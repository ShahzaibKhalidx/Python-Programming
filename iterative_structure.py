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
    if i > 500:
        break
    if i > 150:
        continue
    if  i%5==0:
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



# TASK-9



# TASK-10

word = str(input("Enter a word "))
reverse = word[::-1]
print(reverse)

# TASK-13
name = "muhammad shahzaib"
vowels = 0
consonants = 0
for x in name:
    for i in ["a","e","i","o","u"]:
        if x == i:
            vowels += 1
        else:
            consonants = len(name) - vowels
print(f"vowels={vowels} and consonants={consonants}")
    

# TASK-14

num_inp = int(input("Number of values? "))
value_list = []
for x in range(1,num_inp+1):
    value = input("Enter a value ")
    value_list.append(value)

print(value_list)


# TASK-15

