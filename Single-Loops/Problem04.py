option=0
x=0
while(option!=4):
    print("\n1-cm to ft\n2-km to miles\n3-USD to INR\n4-exit\n")
    option=int(input("Select Option: "))
    if(option==1):
        x=float(input('Enter in cm: '))
        print(f'Feet= {x*0.32808399}')
    elif(option==2):
        x=float(input('Enter in km: '))
        print(f'Miles= {x*0.62137119}')
    elif(option==3):
        x=float(input('Enter in usd: '))
        print(f'INR= {x*85.79}')
    elif(option==4):
        break
    else:
        print("Please Enter a Valid Option(1,2,3, or 4)")
