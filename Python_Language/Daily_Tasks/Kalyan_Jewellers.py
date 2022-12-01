print("Welcome To Kalyan Jewellers")

Name = input("Enter your name : ")
Gender = input("Enter your gender : ")
Age = int(input("Enter your age : "))

print("Name : ",Name)
print("Gender : ",Gender)
print("Age : ",Age)

Product = input("Enter product name : ")
Gram = int(input("Enter gram of product : "))
Gold_price = int(5752)

print("Product : ",Product)
print("Gram : ",Gram)
print("Gold_price : ",Gold_price)

Total_rate = Gram * Gold_price
print("Total_rate : ",Total_rate)

making_charges = int(input("Enter making charges : "))
print("making_charges : ",making_charges)

Total_charges = Total_rate * making_charges
print("total_charges : ",Total_charges)

Total_amt = Total_rate + Total_charges
print("total_amt : ",Total_amt)


Discount = ""

if Gender == "male":
    if Age > 65:
        if Total_amt >= 200000:
            print("Discount 20%")
            Discount = int(Total_amt)*20/100
        elif Total_amt >= 300000:
            print("Discount 30%")
            Discount = int(Total_amt)*30/100
        elif Total_amt > 500000:
            print("Discount 35%")
            Discount = int(Total_amt)*35/100
        else:
            print("No discount")
else:
    if Age < 65:
        if Total_amt >= 200000:
            print("Discount 10%")
            Discount = int(Total_amt)*10/100
        elif Total_amt >= 300000:
            print("Discount 20%")
            Discount = int(Total_amt)*20/100
        elif Total_amt > 500000:
            print("Discount 25%")
            Discount = int(Total_amt)*25/100
    else:
        print("No discount")

if Gender == "female":
    if Age > 65:
        if Total_amt >= 200000:
            print("Discount 25%")
            Discount = int(Total_amt)*25/100
        elif Total_amt >= 300000:
            print("Discount 35%")
            Discount = int(Total_amt)*35/100
        elif Total_amt > 500000:
            print("Discount 40%")
            Discount = int(Total_amt)*40/100
    else:
        print("No discount")
else:
    if Age < 65:
        if Total_amt >= 200000:
            print("Discount 15%")
            Discount = int(Total_amt)*15/100
        elif Total_amt >= 300000:
            print("Discount 25%")
            Discount = int(Total_amt)*25/100
        elif Total_amt > 500000:
            print("Discount 30%")
            Discount = int(Total_amt)*30/100
        else:
            print("No discount")

Dis_amt = (Total_amt - making_charges) - Discount
print("Dis_amt : ",Dis_amt)

Net_amt = Total_amt - Dis_amt
print("Net_amt : ",Net_amt)
























 
















