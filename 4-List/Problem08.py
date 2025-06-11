list1=['CampusX is a channel', 'for data-science', 'aspirants.']
result=[]
for i in list1:
    result.extend(i.split())
print(result)