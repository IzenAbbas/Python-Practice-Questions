def concatenate_dics(*args):
    result={}
    for i in args:
        for key,value in i.items():
            result[key]=value
    return result



dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

result=concatenate_dics(dic1,dic2,dic3)
print(result)