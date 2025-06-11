x=int(input("Enter a Number: "))
result=1
if(x>=0):
    for i in range(1,x+1):
        result*=i

    print(f"Factorial= {round(result,2)}")
else:
    print(f"factorial of {x} is not possible")
