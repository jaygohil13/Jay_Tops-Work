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
while status:
  print(menu)
  menu_choice = int(input("Enter your choice : "))
  if menu_choice == 1:
    print("Banker")
  print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
  print("\t\tWelcome To Banker's App")
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
      else:
        #status = False
        break

  elif Banker_choice == 2:
    print("View Customer")
    




