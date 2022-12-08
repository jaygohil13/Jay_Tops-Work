print("\t\t\t\tWELCOME TO JAY BHAVANI\n\n\n ")


JayBhavani = {
    1 : {
        "Vadapav" : "20",
    },
    2 : {
        "Dabeli" : "30",
    },
    3 : {
        "Bhel" : "70"
    }
}

for i in range(1,len(JayBhavani)+1):
    Customer = input("Customer name : ")
    product_name = input("product name : ")
    Total_Qty = int(input("Enter qty : "))
    price = int(input("Enter your price : "))
    print("price : ",price)
    Total_amt = Total_Qty * price
    print("Total_amt : ",Total_amt)
