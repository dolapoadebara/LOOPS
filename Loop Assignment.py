x=1
while(x<=100):
    if(x%3==0) and (x%5==0):
        print(x,"fizzbuzz")
    elif(x%3==0):
        print(x,"fizz")
    elif(x%5==0):
        print(x,"buzz")
    x+=1
