n=int(input("Enter size of the pattern: "))
c=n
r=0
middle1=0
middle2=0
if(n%2==0):
    r=n//2
    middle1=n//2-1
    middle2=n//2
else:
    r=n//2+1
    middle1=n//2
    middle2=n//2


for i in range(0,r):
    for j in range(0,c):
        if(j<=middle2 and j>=middle1):
            print('*',end='')
        else:
            print(' ',end='')
    middle1-=1
    middle2+=1
    print('')


