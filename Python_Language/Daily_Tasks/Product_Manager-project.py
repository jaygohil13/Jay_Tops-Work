print("\t\t\tPRODUCT_MANAGER_PROJECT\n\n\n")

menu="""
        menu

        press 1 for product manager
        press 2 for customer

"""
print(menu)

status = True
while status:
    product_manager={}
    choice = int(input("Enter your choice (1/2) : "))
    if choice == 1:
        print("product_manager : ")
        product_name = input("Enter product name : ")
        qty = int(input("Enter qty : "))
        price = int(input("Enter price : "))
        Total_price = qty * price
        print("Total_price : ",Total_price)
        product_manager["product_name"] = product_name
        product_manager["qty"] = qty
        product_manager["price"] = price
        print("-----> PRODUCT ",product_manager)
    elif choice == 2:
        print("Customer : ")
    

