inp_1 = int(input("enter digit one of five "))
inp_2 = int(input("enter digit two of five "))
inp_3 = int(input("enter digit three of five "))
inp_4 = int(input("enter digit four of five "))
inp_5 = int(input("enter digit five of five "))
    
inp_list = [inp_1,inp_2,inp_3,inp_4,inp_5]

for x in inp_list:
    if x == x:
        print("DUPLICATE")
    else:
        print("ALL UNIQUE")