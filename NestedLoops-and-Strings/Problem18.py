a=input('Input string A: ').lower()
b=input('Input string B: ').lower()

list_a=a.split()
list_b=b.split()
combined=list_a+list_b
result=list()

for i in combined:
    if combined.count(i)==1:
        result.append(i)

print('Result:',result)