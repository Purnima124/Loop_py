n=int(input("enter the number "))
s=n
i=0
while n>0:
    b=n%10
    i=i*10+b
    n=n//10
if s==i:
    print("palindrom number")
else:
    print("not palindrom number")


