import sys
import gspread
import time
from datetime import datetime
from google.oauth2.service_account import Credentials

# colorama for text formatting
# tutorial: https://linuxhint.com/colorama-python/
import colorama
from colorama import Fore, Back, Style

# initialize colorama
colorama.init(autoreset=True)

# os library to clear screen
import os


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('creamy-cones')
orders_worksheet = SHEET.worksheet("orders")

def prog_start():
    """
    Run opening screen for user and gives brief explanation of its use.
    """
    print("\n")
    # Fore and Style options are colorama properties to give the text colours
    print(Fore.BLUE + Style.BRIGHT + '''
    ###                                               
  ##  ##                                              
 ##        ## ###    ####     #####   ## ##    ##  ## 
##        ####     ##   ##  ##   ##  #######  ##  ##  
##        ##      ######## ##    ##  ## # ##  ##  ##  
##  ##   ##       ##       ##  ###  ##   ##    ####   
 ###     ##        ####     ### ##  ##   ##      ##   
                                              ####    
    ###                                      
  ##  ##                                     
 ##         ####   ## ###     ####     ##### 
##        ##   ##  ###  ##  ##   ##   ##     
##       ##    ##  ##   ## ########    ##    
##  ##   ##   ##  ##   ##  ##           ##   
 ###      ####    ##   ##   ####    #####    
    ''')
    print("\n")
    print(Fore.BLUE + Style.BRIGHT + "           sales & Food Management \n")
    time.sleep(3)
    print(Fore.BLUE + Style.BRIGHT + "(Created for Ordering Purposes -"
          " Copyright: Meghana Vinakota '24)")
    time.sleep(3)
    clearScreen()

# clear screen function
# Credit: https://www.101computing.net/python-typing-text-effect/
def clearScreen():
    """
    Function for clearing CLI for new code
    """
    os.system("clear")

def welcome():
    """
    welcome to the customer or
    leave if customer dont want to order
    """
    while True:
        print("Welcome to Creamy Cones!")
        print("Would you like to order? [Y]es or [N]o\n")
        user_choice = input("Enter: \n")
        user_choice = user_choice.strip()
        if user_choice == "Y" or user_choice == "y":
            print("\nLets take a look on the menu...\n")
            break
        elif user_choice == "N" or user_choice == "n":
            print("See you again!")
            sys.exit()
        else:
            print(Fore.RED + "Please enter the correct choice")
            print("Your choice sholud be Y or N\n")
            return welcome()

class IcecreamMenu:
    """
    Ice cream Flavours menu class type
    """
    def __init__(self, name,flavour):
        self.name = name
        self.flavour = flavour

    def print(self):
        """
        Print selected icecream
        """
        return self.name+" " +self.flavour

class ConeSize:
    """
    Cone size class type
    """
    def __init__(self,label,price):
        self.label = label
        self.price = price

class IcecreamToppings:
    """
    Toppings class type
    """
    def __init__(self,topping):
        self.topping = topping

icecream_menu = {
    "1": IcecreamMenu("Strawberry", "flavour"),
    "2": IcecreamMenu("Vanilla","flavour"),
    "3": IcecreamMenu("Chocolate","flavour"),
    "4": IcecreamMenu("Pistachio","flavour"),
    "5": IcecreamMenu("Mango","flavour"),
    "6": IcecreamMenu("Banana","flavour")
}

cone_size  = {
    "S": ConeSize("Small",3),
    "L": ConeSize("Large",5)
}

icecream_toppings = {
    "C": IcecreamToppings("Chocolatesyrup"),
    "M": IcecreamToppings("Marshmallows"),
    "N": IcecreamToppings("Nuts")
}


def select_icecream():
    """
    To select the flavour of icecream
    """
    for index, icecream in icecream_menu.items():
        print(index, icecream.name)
    print(
        "\nPlease pick the flavour from the menu\n"
        "If you've changed your mind,\n"
        "press E to Exit.\n"
    )
    while True:
        user_input = input("Enter number: \n")
        user_input = user_input.strip().lower()
        if user_input == "e":
            print("See you next time!")
            sys.exit()
            break
        elif user_input in icecream_menu:
            print(
                "\nYou have chosen our",
                icecream_menu[user_input].print(),"\n"
            )
            break
        else:
            print(Fore.RED+
                "\nInvalid!\n")
            print("Please enter number between 1-6 or E\n"
            )
    return icecream_menu[user_input]


def select_size():
    """
    To slect size of cone
    """
    for index, size in cone_size.items():
        print(index, "-", size.label, "-", "€", size.price)
    while True:
        print(
            "\nPlease select the size of cone.\n"
            "Enter either S or L\n"
            "Press E to Exit.\n"
        )
        user_size_input = input("Enter size: \n")
        user_size_input = user_size_input.strip().upper()
        if user_size_input == "E":
            print("See you next time!")
            sys.exit()
            break
        elif user_size_input in cone_size:
            print(
                "\nYou have chosen a ",
                cone_size[user_size_input].label,
                "cone\n"
            )
            break
        else:
            print(Fore.RED+
                "\nInvalid"
            )
    return cone_size[user_size_input]


def select_quantity():
    """
    To slect quantity of cones
    """
    print("\nHow many Ice creams you want to order?\n"
    "You can order upto 8.\n"
    "Press E to Exit.\n")
    while True:
        user_quantity_input = input("Please enter quantity: \n")
        user_quantity_input = user_quantity_input.strip().lower()
        if user_quantity_input == "e":
            print("See you next time")
            sys.exit()
            break
        elif user_quantity_input >= str(1) and user_quantity_input <= str(8):
            print("\nYou have selected a quantity of", user_quantity_input)
            break
        else:
            print(Fore.RED+
                "\nInvalid\n"
            )
    return user_quantity_input


def add_toppings():
    """
    To add toppings
    """
    print("Do you want toppings on your icecream?")
    print("[Y]es or [N]o")
    print("Press E to Exit.\n")
    while True:
        user_toppings_input = input("Enter: \n")
        user_toppings_input = user_toppings_input.strip().upper()
        if user_toppings_input == "Y":
            print("\n Lets take a look at the toppings")
            def select_toppings():
                """
                To select the toppings for icecream
                """
                for index, top in icecream_toppings.items():
                    print(index, "-", top.topping)
                while True:
                    print(
                        "\nPlease select the toppings.\n"
                        "Enter either C , M or N\n"
                        "Press E to Exit.\n"
                    )
                    user_topping_input = input("Enter toppings: \n")
                    user_topping_input = user_topping_input.strip().upper()
                    if user_topping_input == "E":
                        print("See you next time!")
                        sys.exit()
                        break
                    elif user_topping_input in icecream_toppings:
                        print(
                            "\nYou have selected ",
                            icecream_toppings[user_topping_input].topping,
                            
                            "topping\n"
                        )
                        break
                    else:
                        print(Fore.RED+
                            "\nInvalid"
                        )
                    
            topping = select_toppings()

            break
        elif user_toppings_input == "N":
            print("\nNo worries!")
            break
        elif user_toppings_input == "E":
            print("\nSee you next time!")
            sys.exit()
            break
        else:
            print(Fore.RED+"\nThat's not right")
            print("Please enter Y or N\n")

    return user_toppings_input


def total_order(quantity, conesize, icecream, toppings):
    """
   To display the order back to the customer
    """
    print("\nYour order is....\n")
    result = quantity + " x " + conesize.label + " " +  icecream.name
    if quantity == str(1):
        result += " icecream"
    else:
        result += " icecreams"
    if toppings.lower() == "y":
        result += " with topping"
    print(result)
    return result


def total_cost(conesize,quantity):
    """
    To calculate the total cost for icecreams
    """
    total = conesize.price * int(quantity)
    
    print("Total cost: €", total)
    return total


def confirm_order():
    """
    To confirm the order
    """
    print("Please confirm your order")
    print("[Y]es or [N]o")
    print("Press E to Exit.\n")
    while True:
        user_confirm = input("Enter: \n")
        user_confirm = user_confirm.strip().upper()
        if user_confirm == "Y":
            print("\nYour order is confirmed! ")
            break
        elif user_confirm == "N":
            print("\nTry to order again..\n")
            break
        else:
            print(Fore.RED+"\nThat's not right")
            print("Please enter Y or N\n")

    return user_confirm

def customer_name():
    """
   To collect the customer name
    """
    print("\nNow... lets take your details\n")
    while True:
        name = input("Enter your first name: \n").title()
        if name.isalpha():
            break
        else:
            print(Fore.RED+
                "\nPlease make sure you entered your "
                "name correctly"
            )
            print("Try again\n")

    return name

def receipt(order, price,name):
    """
    To generate the receipt
    """
    print("Thank you!\n")
    print("Here is your receipt")
    print("---------------------------------")
    print("Creamy Cones\nMain street\nDublin\n")
    print("Order #")
    print("Customer name:", name)
    print(order)
    print("€" + str(price))
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    print(time)
    print("---------------------------------\n")

    return {"time": time}

def update_spreadsheet(row):
    """
    To update google worksheet with data obtained
    """
    orders_worksheet.append_row(row)

def main():
    """
    Run all program functions
    """
    prog_start()
    welcome()
    while True:
        icecream = select_icecream()
        conesize = select_size()
        quantity = select_quantity()
        toppings = add_toppings()
        order = total_order(quantity, conesize, icecream, toppings)
        price = total_cost(conesize, quantity)
        confirmed = confirm_order()
        if confirmed.upper() == "Y":
            break
    name = customer_name()
    bill = receipt(order,price,name)
    row = [
        name, icecream.name, conesize.label, quantity, toppings, price,
        bill["time"]
    ]
    update_spreadsheet(row)

main()
