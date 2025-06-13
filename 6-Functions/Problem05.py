def is_perfect(num=1):
    divisors=[]
    divisors.append(num)

    for i in range(1,num//2+1):
        if(num%i==0):
            divisors.append(i)
    
    return sum(divisors)/2==num


print('All Perfect Numbers from 1 to 10000')
for i in range(1,10001):
    if(is_perfect(i)):
        print(i)