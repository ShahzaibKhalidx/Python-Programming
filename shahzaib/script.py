f = open("first.txt",'r')
print("starting position",f.tell())
print(f.readline())
#line = int (input("enter num of line you want to  see "))
#print(x[line])
print(f.tell())
f.seek(0)
print(f.tell())
print(f.readline())
