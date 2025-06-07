print("Enter co-ordinates of first point (x1, y1):")
x1= float(input("x1: "))
y1= float(input("y1: "))
print("Enter co-ordinates of second point (x2, y2):")
x2= float(input("x2: "))
y2= float(input("y2: "))

distance = round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5,4)
print(f"The distance between the points ({x1}, {y1}) and ({x2}, {y2}) is: {distance}")