from operation import handle_rent, handle_return
from bill import generate_rent_bill, generate_return_bill, save_rent_bill, save_return_bill

def display_menu():
    """
    Display the main menu for user selection.
    """
    print("Select an option:")
    print("1. Rent Land")
    print("2. Return Land")
    print("3. Exit")

def main():
    """
    Main function to run the land rental system.
    """
    while True:
        display_menu()
        choice = input("Please choose an option (1-3): ")

        if choice == '1':
            rented_lands, customer_name = handle_rent()
            bill_details = generate_rent_bill(rented_lands, customer_name)
            save_rent_bill(bill_details, customer_name)

        elif choice == '2':
            returned_lands, customer_name = handle_return()
            bill_details = generate_return_bill(returned_lands, customer_name)
            save_return_bill(bill_details, customer_name)

        elif choice == '3':
            print("Thank you for using the land rental system. Goodbye!")
            break

        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
