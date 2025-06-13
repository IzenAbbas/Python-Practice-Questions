Str1 = "hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX"
vowels=['a','A','e','E','i','I','o','O','u','U']
s=set()

for i in Str1:
    if i in vowels:
        s.add(i)

print('No of Unique Vowels-',len(s))