ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

s1=set()
s2=set()
s3=set()

for i in ar1:
    s1.add(i)
for i in ar2:
    s2.add(i)
for i in ar3:
    s3.add(i)

common=list(s1.intersection(s2).intersection(s3)) #or simply (s1 & s2 & s3)

print('Common Values: ',common)