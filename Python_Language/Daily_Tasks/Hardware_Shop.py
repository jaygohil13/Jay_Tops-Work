print("\t\t\t\tHARDWARE SHOP\n\n\n\n")

Category = {

    "Laptop"
    "Mobile"
}
def laptop():
    print("\n Items in Laptop")
    print("===================")
    print("1 - Samsung")
    print("2 - HP")
    print("3 - Dell")

choice = input("Enter your choice of laptop you want : ")

def laptop(choice):
    if choice == "Samsung":
        print("price of samsung 4-Gb Ram i5 is 50,000")
    elif choice == "HP":
        print("price of HP 8-GB Ram i7 is 45,000")
    elif choice == "Dell":
        print("price of Dell 8-Gb i7 is 60,000")
    else:
        print("Not Available")


print(laptop(choice))


def mobile():
    print("\n Items in Mobiles")
    print("====================")
    print("1 - Apple")
    print("2 - Samsung")
    print("3 - Vivo")

choice == input("Enter your choice of mobile you want : ")

def mobile(choice):
    if choice == "Apple":
        print("price of Apple 14 pro is 100,000")
    elif choice == "Samsung":
        print("price of Samsung A12 is 40,000")
    elif choice == "Vivo":
        print("price of Vivo V50 is 50,000")
    else:
        print("Not Available")



print(mobile(choice))