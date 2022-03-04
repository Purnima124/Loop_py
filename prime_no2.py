num=int(input("enter number: "))
i=2
count=0
while i<num: 
    if (num%2==0):
       count=count+1
    i=i+1
if count==0:
    print("prime number")
else:
   print("not prime number")
