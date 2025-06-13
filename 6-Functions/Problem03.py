def count_UppLow(s=''):
    u_count=0
    l_count=0
    
    for i in s:
        if i.islower():
            l_count+=1
        elif i.isupper():
            u_count+=1
    
    return (u_count,l_count)


sample="CampusX is an Online Mentorship Program fOr EnginEering studentS."
result=count_UppLow(sample)
print('No. of Upper case characters :',result[0])
print('No. of Lower case Characters',result[1])