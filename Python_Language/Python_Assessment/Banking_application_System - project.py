print("**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**\n")
print("\t\tWELCOME TO PYTHON BANK MANAGEMENT SYSTEM\n")
print("**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**")

menu = """

                    SELECT YOUR ROLE

                      1) Banker
                      2) Customer

                      3) Exit
              

"""
accounts = {}
menu_choice = 0
balance = 0

status = True
total = 0 
while status:
  print(menu)
  menu_choice = int(input("Enter your choice : "))
  if menu_choice == 1:
    print("Banker")
    print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*\n")
    print("\t\tWelcome To Banker's App\n")
    print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")

    menu = """
                  Operations Menu

                  1) Add Customer
                  2) View Customer
                  3) Search Customer
                  4) View All Customer
                  5) Total Amounts in Bank
    
    """
    print(menu)

    Banker_choice = int(input("Enter your choice : "))
    if Banker_choice == 1:
      spec = {}
      print("Add Customer")
      account_no = int(input("Enter your account no : "))
      name = input("Enter your name : ")
      balance = int(input("Enter your opening balance : "))
      
      if account_no in accounts.keys():

        spec['name'] = name
        spec['balance'] = balance

        accounts[account_no] = spec
        print("---->>>Already exist",accounts)

      else:
        spec['name'] = name
        spec['balance'] = balance

        accounts[account_no] = spec

        print(accounts)
        ch = input("Do you want to perform more operations (y/n) : ")
        if ch == 'y':
          continue
      
       
    elif Banker_choice == 2:
      print("View Customer")
      spec = {}
      if account_no in accounts.keys():

        spec['name'] = name
        spec['balance'] = balance

        accounts[account_no] = spec
        print("---->>>Customers",accounts)

      else:
        spec['name'] = name
        spec['balance'] = balance

        accounts[account_no] = spec

        print(accounts)
    
    elif Banker_choice == 3:
      print("Search Customer")

      no = input("Enter account no  : ")
      i = accounts[account_no]
      print(i['name'])
      print(i['balance'])

    elif Banker_choice == 4:
      print("View All Customer")
      spec = {}
      if account_no in accounts.keys():

        spec['name'] = name
        spec['balance'] = balance

        accounts[account_no] = spec
        print("---->>> View All Customers",accounts)

      else:
        spec['name'] = name
        spec['balance'] = balance

        accounts[account_no] = spec

        print(accounts)
    

    elif Banker_choice == 5:
      for k,v in accounts.items():
        total += accounts[account_no]['balance']

      print("Total Amount in Bank : ",total)

    else:
      print("Invalid input not in  banker menu ")
  
  elif menu_choice == 2:
    print("Customer")
    print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=\n")
    print("\t\tWelcome To Customer's App\n")
    print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=")
  
    menu = """
  
            Operations Menu

            1) Withdraw Amount
            2) Deposite Amount
            3) View Balance
  
  """
    print(menu)
  
    Customer_choice = int(input("Enter your choice :"))
    if Customer_choice == 1:
     print("Withdraw Amount")

    elif Customer_choice == 2:
     print("Deposite Amount")

    elif Customer_choice == 3:
     print("View Balance")
  
    else:
     print("Invalid input not in customer menu")


  elif menu_choice == 3:
    print("Exit")
    
  status = False





