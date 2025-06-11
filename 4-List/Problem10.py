list1=['campusxIs', 'bestFor', 'dataScientist']

result=[[] for i in range(len(list1))]

for i in range(len(list1)):
    for j in list1[i]:
        if(j.isupper()):
            result[i].append(' ')
        result[i].append(j)

for i in range(len(result)):
    result[i]=''.join(result[i])
result=' '.join(result)

print(result)

