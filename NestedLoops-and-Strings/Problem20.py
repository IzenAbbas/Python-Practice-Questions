str=input('Input the String: ')
n=len(str)
flag=[]
result=''
for i in str:
    flag.append(True)

for i in range(0,n):
    for j in range(i+1,n):
        if(flag[i] and str[i]==str[j]):
            flag[j]=False

for i in range(0,n):
    if(flag[i]):
        result+=str[i]
print('Result: ', result)