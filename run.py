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

def main():
    """
    Run all program functions
    """
    welcome()


main()
