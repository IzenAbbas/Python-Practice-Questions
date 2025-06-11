salary=float(input("Enter Salary: "))

#calculating hra, df and pfa
hra=salary*0.1
df=salary*0.05
pfa=salary*0.03

salary=salary-hra-df-pfa
#calculating 10%, 20% and 30% of salary
temp10=salary*0.90
temp20=salary*0.80
temp30=salary*0.70



if(salary>=500000 and salary<1000000):
    salary=temp10
elif(salary>=1000000 and salary<2000000):  
    salary=temp20
elif(salary>=2000000):
    salary=temp30


print(f"Monthly Salary after tax-deduction is: {round(salary/12,2)}")