str1='My name is Izen'
vowels='aeiou'
result=''.join(list(filter(lambda i: i.lower() not in vowels,str1)))
print(result)