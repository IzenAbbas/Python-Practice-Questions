x=input('Enter a String: ')
sum=0
count=1
avg=0

for i in x:
    if(i.isnumeric()):
        sum+=int(i)
        count+=1
avg=sum/count
print('Sum: ',sum)
print('Average: ',avg)