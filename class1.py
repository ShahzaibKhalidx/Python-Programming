Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("Hello World")
Hello World
x=["car","bike","ship"]
print(x)
['car', 'bike', 'ship']
type(x)
<class 'list'>
y=("eng","math","phy")
type(y)
<class 'tuple'>
print(y)
('eng', 'math', 'phy')
x = range(6)
print(x)
range(0, 6)
x = range("5")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    x = range("5")
TypeError: 'str' object cannot be interpreted as an integer
tuple1 = (1,2,3,4,5)
print(tuple1)
(1, 2, 3, 4, 5)




tuple2 = ("a","b","c")
print(tuple2)
('a', 'b', 'c')
type(tuple2)
<class 'tuple'>
x = {"name" : "John", "age" : 36}
print(x)
{'name': 'John', 'age': 36}
print(x.name)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print(x.name)
AttributeError: 'dict' object has no attribute 'name'
x = {"name" : "asad", "age" : 24, "class" : 9}
print(x)
{'name': 'asad', 'age': 24, 'class': 9}
print(x(name))
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print(x(name))
NameError: name 'name' is not defined
x = {a : 1, b : 2, c: 3}
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    x = {a : 1, b : 2, c: 3}
NameError: name 'a' is not defined
x = {"a" : 1, "b" : 2, "c" : 3}
print(x)
{'a': 1, 'b': 2, 'c': 3}
x = True
print(x)
True
x = False
print(x)
False
str (6)
'6'
int (25.6)
25
float (3)
3.0
complex (6)
(6+0j)
complex (x)
0j
list ("a")
['a']
list (("a","b","c"))
['a', 'b', 'c']
x
False
x = dict(name="John",age=36)
x
{'name': 'John', 'age': 36}
x = bool(5)
x
True
x = bool(0)
x
False

= RESTART: E:/PGD/PythonProgramming/code/first.py
Five is greater than two!
a,b,c = 'I','love','pakistan',2
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a,b,c = 'I','love','pakistan',2
ValueError: too many values to unpack (expected 3)
a,b,c = 'I','love','pakistan'
print(a,b,c)
I love pakistan
d=e=f='world'
print(a)
I
print(d)
world
a='world'
print(a)
world
a
'world'
e
'world'
f
'world'
id(d)
1761156124400
id(e)
1761156124400
id(a)
1761156124400
x= y= [1,2]
z=[1,2]
id(z)
1761156169920
id(y)
1761155860864
id(x)
1761155860864
fruits = ["a","b","c"]
x,y,z = fruits
x
'a'
y
'b'
z
'c'
x= "apple"
y= "banana"
z= "cherry"
>>> fruits = x,y,z
>>> fruits
('apple', 'banana', 'cherry')
>>> type(fruits)
<class 'tuple'>
>>> complex (1j)
1j
>>> complex(5)
(5+0j)
>>> import random
>>> print(random.randrange(5,500))
121
