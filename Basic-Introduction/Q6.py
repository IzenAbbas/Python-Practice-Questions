heads=int(input("Enter the number of heads: "))
legs=int(input("Enter the number of legs: "))
Chickens=0
dogs=0

#first calculating hens by assigning 2 legs to each hed
for i in range(0,heads):
    legs-=1
    if(legs<=0):
        break
    legs-=1
    if(legs<=0):
        Chickens+=1
        break
    Chickens+=1

#then assigning 2 more legs to each head to test that whether it can become a dog or not
for i in range(0,heads):
    legs-=1
    if(legs<=0):
        legs+=1
        break
    legs-=1
    if(legs<=0):
        dogs+=1
        Chickens-=1
        break
    dogs+=1
    Chickens-=1

#if all of the legs and all of the heads are not used in combinations, then give an error
if(legs>0 or (Chickens+dogs)!=heads):
    print("Invalid Combination of Heads and Legs")
else:
    print(f'Chickens: {Chickens}')
    print(f'Dogs: {dogs}')
