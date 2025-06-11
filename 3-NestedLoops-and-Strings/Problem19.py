str=input('Enter the String: ')
sub=input('Enter a word: ')
list_str=str.split()
loc=-1
index=1
for x in list_str:
    if sub==x:
        loc=index
        break
    index+=1
if(loc!=-1):
    print(f'Location of word is {loc}')
else:
    print(sub, 'is not present')
