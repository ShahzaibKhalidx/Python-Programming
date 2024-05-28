
def calc () :
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

    
