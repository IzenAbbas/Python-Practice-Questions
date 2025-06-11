list1=[[1,2,3],[4,5,6],[7,8,9]]
max_per_row=[0]*len(list1)
for i in range(len(list1)):
    max_per_row[i]=max(list1[i])
print('Max of eac Row:',max_per_row)