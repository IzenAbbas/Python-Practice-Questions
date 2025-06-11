list1=[2,4,6,10,1]
result=[]
for i in range(len(list1)):
    sum=0
    sum+=list1[i]
    for j in range(len(list1)):
        if(i!=j and list1[i]<list1[j]):
            sum+=list1[j]
    result.append(sum)

print(result)