x=input('Enter a string: ')
if(x[:len(x)//2]==x[len(x)//2:]):
    print('{} is symmitrical'.format(x))
else:
    print('{} is not symmitrical'.format(x))