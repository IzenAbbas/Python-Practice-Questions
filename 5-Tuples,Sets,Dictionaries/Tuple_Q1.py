#Solution#1
test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
flag=[True]*len(test_list)
result=[]

for i in range(len(test_list)):
    if(flag[i]):
        temp=[test_list[i][0]]
    else:
        continue
    for j in range(i,len(test_list)):
        if(test_list[i][0]==test_list[j][0] and flag[j]):
            temp.append(test_list[j][1])
            flag[j]=False
    result.append(tuple(temp))

print('Output by first method:\t',result)

#Solution#2
test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
keys=set()
key_list_pairs={}

for i in test_list:
    if i[0] not in keys:
        keys.add(i[0])

for i in keys:
    temp1=[]
    for j in test_list:
        if(i==j[0]):
            temp1.append(j[1])
    key_list_pairs[i]=temp1

result=[]
for i in keys:
    temp2=[i]
    for j in key_list_pairs[i]:
        temp2.append(j)
    result.append(tuple(temp2))

print('Output by second method:',result)