#29-->password genrator engine

password1=0
while password1!="strong":
    up=0
    low=0
    spe=0
    num=0
    length=0
    password=input("enter password: ")
    for i in password:
        if 48<=ord(i)<=57:
            num+=1
        elif 65<=ord(i)<=90:
            up+=1
        elif 97<=ord(i)<=122:
            low+=1
        else:       
            spe+=1
        length+=1
    if length>8:
        if length<20:
            if num>0:
                if low>0:
                    if up>0:
                        if spe>0:
                            print("your password is strong")
                            password1="strong"
                        else:
                            print("password doesn't have special characters")
                            password1="not strong"
                    else:
                        print("password doesn't have upper characters")
                        password1="not strong"
                else:       
                    print("password doesn't have lower characters")
                    password1="not strong"
            else:
                print("password doesn't have numbers")
                password1="not strong"
        else:
            print("password id long")
            password1="not strong"
    else:   
        print("password is short")
        password1="not strong"