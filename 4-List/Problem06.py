num1 = [23,45,67,78,89,34]
num2 = [34,89,55,56,39,67]
result=[i for i in num1 if i in num2 if(num1.count(i)==1 and num2.count(i)==1)]
result.sort()
print(result)