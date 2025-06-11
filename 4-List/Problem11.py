list1=[1,2,3,4,5,1]
list2=[2,3,5,7,8]
merged=list1+list2
union=[]
for i in merged:
    if i not in union:
        union.append(i)
union.sort()
print('Union:', union)

