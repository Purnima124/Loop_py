i=0
while i<100:
    num=int(input("enter the number "))
    if num==1:
        print(num,"nutural no.")
    elif num%2!=0:
        print(num,"odd number")
    elif num%2==0:
        print(num,"even number")
    elif num==0:
        print(num,"whole number")
    i=i+1


