pwd = input("Enter your password! ")

if 7<len(pwd)<15:
    if '@' in pwd and '$' in pwd:
        if '0' in pwd and '1' in pwd:
            print("Password is Perfect!")
        else:
            print("add a number!")
    else:
        print("add special character!")
else:
    print("Length must be 7 to 15")
            
