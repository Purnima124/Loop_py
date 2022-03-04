i=0
while i<=30:
    if i%3==0 and i%21==0:
        print(i,"bye")
    elif i%3==0:
        print(i,"hi")
    elif i%7==0:
        print(i,"helo")
    else:
        print(i,"ok")
    i=i+1
