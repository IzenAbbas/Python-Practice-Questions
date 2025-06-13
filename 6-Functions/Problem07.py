def max_occurence(s):
    max_occur=0
    max_word=''

    for i in s.split():
        temp_count=s.count(i)
        print(i,temp_count)
        if(temp_count>max_occur):
            max_occur=temp_count
            max_word=i
    
    return (max_word,max_occur)



str1="hello how are you i am fine thank you"

result=max_occurence(str1)
print(result[0],'->',result[1])