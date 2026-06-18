# taking input from user for P Q R 
p=int((input("enter the value of p ")))
r=int((input("enter the value of q ")))
t=int((input("enter the value of r ")))
#calculating the amount
a=p*(1+r/100)**t
print(a)
#calculating the compound intrest 
CI = a - p
print(CI)