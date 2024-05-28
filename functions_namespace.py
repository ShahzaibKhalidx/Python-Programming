def my_func (**kwargs):
    for item in kwargs.items() :
        print (item)
my_func (first='computer', last='programming')


def arg_func (*kids) :
    print("the youngest kid", kids[3])

arg_func ('asad','bilal','hira','wasiq')


def my_print (*args) :
    for value in args :
        print (value)

#my_print ('learning','python','3',)

#my_print ('learning','python','3','and','java','too')


def adder (n, *args) :
    summ = 0
    for value in args :
        summ += value
    return summ / n
    
print(adder(2,4,5,3,6))


#import math,random
from math import *

x = sqrt(56)
print('sqrt ',x)



    



