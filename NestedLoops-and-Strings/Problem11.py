x=input('Enter a String: ')
temp=x.split()
result=''
for i in range(0,len(temp)):
    result+=temp[i][0]
result=result.upper()
print('Short Form:',result)