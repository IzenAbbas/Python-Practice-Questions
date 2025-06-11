n=int(input('Enter n: '))
sum=0
term=''
print('Sum= ',end='')
for i in range(0,n):
    term=term+'2'
    if(i==n-1):
        print(term, end=' = ')
    else:
        print(term, end=' + ')
    sum+=int(term)
print(sum)
