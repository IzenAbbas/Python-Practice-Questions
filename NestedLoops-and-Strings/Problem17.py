x=input("Enter a String: ")
temp_list1=x.split()
temp_list2=list()
temp_str=''
n=len(temp_list1)
for i in range(n-1,-1,-1):
    temp_list2.append(temp_list1[i])

x=' '.join(temp_list2)
print("Reversed:",x)