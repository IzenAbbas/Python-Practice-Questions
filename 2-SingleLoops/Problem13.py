start=int(input('Enter Start of range: '))
end=int(input('Enter End of range: '))
end+=1
for i in range(start,end):
    sum=0
    num=i
    while(num>0):
        sum+=(num%10)**3
        num//=10
    if(sum==i):
        print(i, end=', ')