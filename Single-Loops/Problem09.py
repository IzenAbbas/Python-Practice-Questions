#There are two Questions labeled as Problem#09 in the set-02

#Solution for first question
num=1
sum=0
count=0
while(num!=0):
    num=int(input('Enter a Number: '))
    sum+=num
    count+=1
print(f"sum= {sum}")
print(f'average= {round(sum/(count-1),2)}')


#Solution for second question
for i in range(2000,3201):
    if(i%7==0 and i%5!=0):
        print(i,end=',')