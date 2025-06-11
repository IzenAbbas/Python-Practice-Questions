x=int(input('Enter a Number: '))
end=int(x**0.5)+1

isPrime=True
for i in range(2,end):
    if(x%i==0):
        isPrime=False
        break

if(isPrime and x>1):
    print(f'{x} is a Prime')
else:
    print(f'{x} is not a Prime')