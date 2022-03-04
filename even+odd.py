num1=int(input("enter the frist number "))
num2=int(input("enter the second number "))
i=1
a=num1+num2
while i<=a:
    if i%2==0:
        print(i,"even")
        i=i+1
    else:
        print(i,"odd")
    i=i+1

