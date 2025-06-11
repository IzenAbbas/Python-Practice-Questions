list1 = ["M", "na", "i", "Kh"]
list2 = ["y", "me", "s", "an"]
result=list(zip(list1,list2))
result=[list(i) for i in result]
print(result)