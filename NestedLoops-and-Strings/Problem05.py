n=int(input("Input n: "))
x=int(input("Input x: "))
n+=1
sum=1

print('sum = 1 +',end='')
for i in range(2,n):
    sum+=(x**i)/i
    if(i==n-1):
        print(f'({x}^{i})/{i}',end=' = ')
    else:
        print(f'({x}^{i})/{i}', end=' + ')
print(round(sum,2))