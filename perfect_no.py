n=int(input("enter a number "))
s=0
i=1
while i<n:
    if n%i==0:
        s=s+i
    i=i+1
if s==n:
    print(n,"perfect number")
else:
    print(n,"not perfect number")
