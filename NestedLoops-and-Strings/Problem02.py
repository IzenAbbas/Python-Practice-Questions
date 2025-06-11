n=int(input("Enter the size of the pattern: "))
if(n%2!=0):
    temp=n//2+1
else:
    temp=n//2
#Printing upperhalf
for i in range(0,temp):
    for j in range(0,temp):
        if(i>=j):
            print('*',end='')
    print('')
#printing lowerhalf
temp=n-temp
for i in range(temp,0,-1):
    for j in range(1,temp+1):
        if(i>=j):
            print('*',end='')
    print('')
        