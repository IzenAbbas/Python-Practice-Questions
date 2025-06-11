x=input('Enter a string: ')
result=''

for i in x:
    if(i.islower()):
        result+=i
for i in x:
    if(i.isupper()):
        result+=i

print('Result:', result)