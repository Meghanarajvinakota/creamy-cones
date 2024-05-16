import sys
import gspread
from google.oauth2.service_account import Credentials

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
            print("Please enter the correct choice")
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

icecream_menu = {
    "1": IcecreamMenu("Strawberry", "flavour"),
    "2": IcecreamMenu("Vanilla","flavour"),
    "3": IcecreamMenu("Chocolate","flavour"),
    "4": IcecreamMenu("Pistachio","flavour"),
    "5": IcecreamMenu("Mango","flavour"),
    "6": IcecreamMenu("Banana","flavour")
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
            print("see you next time!")
            sys.exit()
            break
        elif user_input in icecream_menu:
            print(
                "\nYou have chosen our",
                icecream_menu[user_input].print(),"\n"
            )
            break
        else:
            print(
                "\nInvalid!\n"
                "Please enter number between 1-6 or E\n"
            )
    return icecream_menu[user_input]


def main():
    """
    Run all program functions
    """
    welcome()
    icecream = select_icecream()


main()
