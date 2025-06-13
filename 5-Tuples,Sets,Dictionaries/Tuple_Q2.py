t=(1, 5, 7, 8, 10)
if(len(t)==0):
    output=()
    print('Output:',output)
    exit()
elif(len(t)==1):
    output=(t[0],)
    print('Output:',output)
    exit()
output=[]
for i in range(len(t)):
    if(i==0):
        output.append(t[0]*t[1])
    elif(i==len(t)-1):
        output.append(t[i]*t[i-1])
    else:
        output.append(t[i-1]*t[i]+t[i]*t[i+1])
output=tuple(output)
print(output)
