h=int(input('Enter Hours of Clock(1-12): '))
m=int(input('Enter Mins of Clock(0-60): '))

angle=30*h-(11/2)*m
if(360-angle>angle):
    print(angle)
else:
    print(360-angle)

