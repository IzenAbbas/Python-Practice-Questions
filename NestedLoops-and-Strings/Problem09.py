dec=int(input("Enter decimal: "))
result=''
is_neg=False

if(dec==0):
    print('Binary: 0')
    exit()

if(dec<0):
    dec*=-1
    is_neg=True

while(dec>0):
    result+=str(dec%2)
    dec//=2

if(is_neg):
    print(f'Binary: -{result[-1::-1]}')
else:
    print('Binary: ',result[-1::-1])