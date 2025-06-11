list1=['1ac21', '23fg', '456', '098d','1','kls']
products=[]

for i in list1:
    product=1
    for j in i:
        if j.isdigit():
            product*=int(j)
    products.append(product)
print(products)

for i in range(len(list1)-1):
    for j in range(i+1,len(list1)):
        if(products[i]<products[j]):
            list1[i],list1[j]=list1[j],list1[i]
            products[i],products[j],=products[j],products[i]

print(products)
print(list1)
