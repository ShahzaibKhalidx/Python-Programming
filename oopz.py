#class Power:
#    exponent = 0
#    base = 0

#    def find_power (self):
#        result = 1
#        for i in range (self.exponent):
#            result = result*self.base
#        print(result)

#P1=Power()
#P1.exponent=2
#P1.base = 3
#P1.find_power()


class Power:

    def set_base (self, x) :
        self.__base = x
    def set_exponent (self, y) :
        self.__exponent = y
    def get_base () :
        print(self.__base)
    def get_exponent () :
        print (self.__exponent)
    def find_power (self) :
        result = 1
        for i in range (self.__exponent) :
            result = result*self.__base
            print( result )

P2=Power ()
P2.set_base(3)
P2.set_exponent(2)
P2.exponent = 2
P2.base = 3
P2.find_power()


class TestPrivate:
    def setPrivateAttr(self, x) :
        self.__privateAttr = x
    def getPrivateAttr(self) :
        return self.__privateAttr
    def __privateMethod(self) :
        print("I am a private method")

p2 = TestPrivate()
p2.setPrivateAttr(44)
#p2.__privateMethod()
p2._TestPrivate__privateMethod()

# class MyClass:
#   x = 5

# p1 = MyClass()
# print(p1.x)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name}:({self.age})"

# p1 = Person('Shahzaib',25)
# p2 = Person('Asad', 24)
# p3 = Person('Bilal', 20)

# print(p1)

# class Point:
#   x = 0
#   y = 0
  
#   def setx(self, xcoord):
#     self.x = xcoord
#   def sety(self, ycoord):
#     self.y = ycoord
#   def wet(self):
#     return self.x, self.y
#   def move(self, dx, dy):
#     self.x += dx
#     self.y += dy

# p1 = Point()
# print(p1.wet())
# p1.setx(4)
# p1.sety(7)
# print(p1.wet())
# p1.move(1,1)
# print(p1.wet())



# class Animal:
#   species = 'cat'
#   language = 'meow'


class Worker:

  def setHoursWorked(self, h):
    self.__hoursWorked = h
  def changeRate(self, r):
    self.__wageRate = r
  def pay(self):
    return (self.__hoursWorked * self.__wageRate)


w1 = Worker()
w1.setHoursWorked(6)
w1.changeRate(2)
print(w1.pay())
