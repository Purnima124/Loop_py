num=int(input("enter number"))
i=2
while i<num:
    if num%i==0:
        print("not prime no.")
        break
    i=i+1
else:
    print("prime no.")

