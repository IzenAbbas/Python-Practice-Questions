n=8
x=int(input("Input x: "))
sum=0

for i in range(1,n):
    sum+=(1/i)*(((x-1)/x)**i)

print(f'Logarithm of {x} approximated to 7 terms is: {round(sum,2)}')