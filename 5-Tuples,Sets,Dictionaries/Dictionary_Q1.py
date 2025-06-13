test_dict = {"CampusX" : [5, 7, 9, 4, 0], "is" : [6, 7, 4, 3, 3], "Best" : [9, 9,6, 5, 5]}

max_count=0
key=''
for i,j in test_dict.items():
    s=set()
    for x in j:
        s.add(x)
    if(len(s)>max_count):
        max_count=len(s)
        key=i

print(key)