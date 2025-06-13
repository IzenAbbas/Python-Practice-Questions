str1=input('Enter a string: ')
s=set()

for i in str1:
    s.add(i)

if(len(s)<=2):
    print('Yes')
else:
    print('No')