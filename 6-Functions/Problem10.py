def bow(str1):
    print(str1.replace('.','').split())

    list1=str1.replace('.','').split()

    return {i:list1.count(i) for i in list1}



str1="John likes to watch movies. Mary likes movies too. Mary also likes to watch football games."
print(bow(str1))