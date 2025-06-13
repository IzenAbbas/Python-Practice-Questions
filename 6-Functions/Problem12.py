list1 = [1,2,3,4,5,6]

#by using list comprehension
result1=[list1[i]**i for i in range(len(list1))]
print(result1)

#by using map()
result2=list(map(lambda index:list1[index]**index,range(len(list1))))
print(result2)