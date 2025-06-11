x=input('Enter a String: ')
temp=''
for i in x:
    if(i.isnumeric()):
        temp+=i
x=str(temp)
del temp
print('Updated String:', x)