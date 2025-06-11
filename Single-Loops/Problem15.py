l1_x = int(input("Enter x-coordinate of top-left corner of first rectangle (L1): "))
l1_y = int(input("Enter y-coordinate of top-left corner of first rectangle (L1): "))
r1_x = int(input("Enter x-coordinate of bottom-right corner of first rectangle (R1): "))
r1_y = int(input("Enter y-coordinate of bottom-right corner of first rectangle (R1): "))
l2_x = int(input("Enter x-coordinate of top-left corner of second rectangle (L2): "))
l2_y = int(input("Enter y-coordinate of top-left corner of second rectangle (L2): "))
r2_x = int(input("Enter x-coordinate of bottom-right corner of second rectangle (R2): "))
r2_y = int(input("Enter y-coordinate of bottom-right corner of second rectangle (R2): "))

if r1_x < l2_x or r2_x < l1_x:
    print("Rectangles Do Not Overlap")
elif r1_y > l2_y or r2_y > l1_y:
    print("Rectangles Do Not Overlap")
else:
    print("Rectangles Overlap")
