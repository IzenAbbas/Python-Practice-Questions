test_str = 'CampusX best for DS students.'
repl_dict = {"best" : "is the best channel", "DS" : "Data-Science"}

test_lst=test_str.split()

for i,j in repl_dict.items():
    if i in test_lst:
        test_str=test_str.replace(i,j)

print(test_str)