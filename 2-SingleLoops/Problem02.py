x=int(input("Enter Angle(alpha): "))
y=int(input("Enter Angle(beta): "))
z=int(input("Enter Angle(gamma): "))


if x>0 and y>0 and z>0 and (x+y+z)==180:
    print(f"alpha={x}, beta={y} and gamma={z} can form a triangle")
else:
    print(f"alpha={x}, beta={y} and gamma={z} cannot form a triangle")