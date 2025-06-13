given={'c': [3], 'b': [12, 10], 'a': [19, 4]}
result=[[]for i in given]

index=0
for i,j in given.items():
    result[index].append(i)
    result[index].append(j)
    index+=1

result.sort()
for i in range(len(result)):
    result[i][1].sort()
    result[i]=tuple(result[i])
    
result=dict(result)
print(result)

