list1 = [1,2,3,4,5,6]
sum=0
for i in range(0,len(list1)):
    sum+=list1[i]
    list1[i]=sum
print(list1)