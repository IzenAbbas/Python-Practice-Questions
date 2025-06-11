cost_price=float(input("Enter cost price:\t"))
selling_price=float(input("Enter selling price:\t"))

if(selling_price>cost_price):
    print("It is a Profit")
elif(selling_price==cost_price):
    print("There is neither profit nor loss")
else:
    print("It is a loss")