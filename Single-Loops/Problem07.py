num=int(input('Enter an Integer: '))
result=0
if(num>=0):
    while(num>0):
        result*=10
        result+=num%10
        num=int(num/10)
    print(result)
else:
    num*=-1
    while(num>0):
        result*=10
        result+=num%10
        num=int(num/10)
    result*=-1
    print(result)