num=int(input("enter the number "))
rev=0
i=num
while num>0:
    rev=(rev*10)+num%10
    num=num//10
if (i==rev):
    print("palindrom no.")
else:
    print("not palindrom no.")
