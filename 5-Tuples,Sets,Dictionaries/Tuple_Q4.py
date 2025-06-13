list1 = [{'hi', 'bye'},{'Geeks', 'forGeeks'},('a', 'b'),['hi', 'bye'],['a', 'b']]
l_count=0
t_count=0
s_count=0
for i in list1:
    if(type(i)==type(list())):
        l_count+=1
    elif(type(i)==type(tuple())):
        t_count+=1
    elif(type(i)==type(set())):
        s_count+=1
print('List-',l_count)
print('Set-',s_count)
print('Tuple-',t_count)
