gender=input("enter the (M/F)")
age=int(input("enterr the age:"))

if(gender=='F'):
    if(age>=18):
        print("eligible for marraige")
    else:
            print("not eligible")
else:            
    if(gender=='M'):
        if(age>=21):
         print("eligible for marraige")
    else:
            print("not eligible")
