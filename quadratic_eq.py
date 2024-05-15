# a = float((input("Enter value of 'a': ")))
# b = float((input("Enter value of 'b': ")))
# c = float((input("Enter value of 'c': ")))
a = 3
b = 4
c = 6

var_1 = b * b
var_2 = 4 * a * c
var_3 = 2 * a
var_4 = var_1 - var_2
square_root = var_4**(1/2)
print("Square Root: ",square_root)

root_1 = - b + square_root / var_3
root_2 = - b - square_root / var_3

answer = root_1 , root_2
print("Answer: ",answer)
