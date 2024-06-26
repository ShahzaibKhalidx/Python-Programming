"""A simple calculator module with multiple functions to perform basic arithmetic operations.

This module contains three functions:
- `calc()`: A simple calculator that takes two numbers and an operator as input and returns the result of the operation.
- `calculator(num1, opr, num2)`: A function that takes two numbers and an operator as arguments and prints the result of the operation.
- `my_calc()`: A text-based calculator that displays a menu of operations and takes user input to perform the selected operation.

Example usage:

```python
>>> from calc_module import calc, calculator, my_calc
>>> result = calc()
Enter first number: 5
Enter the operand! +
Enter second number: 3
8
>>> calculator(5, '+', 3)
Result 8
>>> my_calc()
1. Addition
2. Subtract
3. Multiply
4. Divide
Enter you input from 1,2,3,4.....5
First number 5
Second number 3
Invalid choice!
1. Addition
2. Subtract
3. Multiply
4. Divide
Enter you input from 1,2,3,4.....2
First number 5
Second number 3
Result 2

"""

def calc () :
    """A simple calculator that takes two numbers and an operator as input and returns the result of the operation.

    Returns:
        int or float: The result of the arithmetic operation.

    """
    inp1 = int(input('Enter first number: '))
    opr = input('Enter the operand! ')
    inp2 = int(input('Enter second number: '))
    ans = 0
    if opr == '+' :
        ans = inp1 + inp2
        return ans
    elif opr == '-' :
        ans = inp1 - inp2
        return ans
    elif opr == 'x' or opr == '*':
        ans = inp1 * inp2
        return ans
    elif opr == '/' :
        ans = inp1 / inp2
        return ans
    print(ans)

def calculator(num1,opr,num2):
    """A function that takes two numbers and an operator as arguments and prints the result of the operation.

    Args:
        num1 (int or float): The first number.
        opr (str): The arithmetic operator.
        num2 (int or float): The second number.

    """
    if opr == '+':
        print ("Result",num1 + num2)
    elif opr == '-':
        print ("Result",num1 - num2)
    elif opr == '*':
        print ("Result",num1 * num2)
    elif opr == '/':
        print ("Result",num1 / num2)

def my_calc():
    """A text-based calculator that displays a menu of operations and takes user input to perform the selected operation.

    """
    print("1. Addition")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = int(input("Enter you input from 1,2,3,4...."))
    num1 = float(input("First number "))
    num2 = float(input("Second number "))
    if choice == 1:
        print("Result", num1+num2)
    elif choice == 2:
        print("Result", num1-num2)
    elif choice == 3:
        print("Result: ", num1 * num2)
    elif choice == 4:
        if num2 == 0:
            print("Can't divide by zero")
        else:
            print("Result: ", num1 / num2)
    else:
        print("Invalid choice!")