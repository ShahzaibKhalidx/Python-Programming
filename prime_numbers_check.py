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
