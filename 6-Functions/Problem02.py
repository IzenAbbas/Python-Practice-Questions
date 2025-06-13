def sort_str1(s):
    l=s.split('-')
    l.sort()
    return '-'.join(l)

str1="green-red-yellow-black-white"
print(sort_str1(str1))