n=int(input("Enter N: "))
sum=0

if n>=1:
    for i in range(1,n+1):
        sum+=i*i
    print(f"sum of squares of first {n} natural numbers is: {sum}")
else:
    print(f'{n} is not a natural number')