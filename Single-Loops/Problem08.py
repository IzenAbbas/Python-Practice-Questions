n=int(input("Enter an integer: "))
sum=0
i=1
while(i<=n and sum<=300):
    if(i%5!=0):
        sum+=i
    i+=1
if(sum>300):
    sum-=i-1
print(sum)
