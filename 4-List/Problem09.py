list1=[['c', 'a', 'm', 'p', 'u', 'x'], ['i', 's'], ['b', 'e', 's', 't'], ['c', 'h', 'a', 'n', 'n', 'e', 'l']]
result=[]

for i in list1:
    result.append(''.join(i))

result=' '.join(result)
print(result)