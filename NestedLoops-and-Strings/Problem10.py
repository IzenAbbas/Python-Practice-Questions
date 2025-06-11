num1=int(input('Enter First Number:\t'))
num2=int(input('Enter Second Number:\t'))
num1=abs(num1)
num2=abs(num2)
min=min(num1,num2)
lcm=0
hcf=0

if num1==0 or num2==0:
    hcf=max(num1,num2)
    lcm=0
else:
    for i in range(1,min+1):
        if(num1%i==0 and num2%i==0):
            hcf=i
    i=1
    while(True):
        if(i%num1==0 and i%num2==0):
            lcm=i
            break
        i+=1
print(f'HCF: {hcf}\nLCM: {lcm}')