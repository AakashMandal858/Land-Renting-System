from datetime import datetime
from read import load_land_records, display_land_records
from bill import generate_rent_bill, generate_return_bill, save_rent_bill, save_return_bill

def handle_rent():
    """
    Handles the process of renting land.
    
    Returns:
        tuple: A tuple containing the list of rented lands and the customer's name.
    """
    land_records = load_land_records()
    rented_lands = []

    while True:
        display_land_records()
        land_id = input("Enter the ID of the land you want to rent: ")

        if not land_id.isnumeric() or int(land_id) < 1 or int(land_id) > len(land_records):
            print("Invalid ID. Please enter a valid land ID.")
            continue

        idx = int(land_id) - 1

        if land_records[idx][-1].strip() == "Available":
            months = input("Enter the number of months you want to rent the land for: ")

            if not months.isnumeric() or int(months) <= 0:
                print("Invalid input. Please enter a positive number for months.")
                continue

            total_price = int(land_records[idx][4]) * int(months)
            land_records[idx][-1] = "Not Available"
            rented_lands.append([*land_records[idx][:4], months, total_price])

            with open('land_data.txt', 'w') as file:
                for record in land_records:
                    file.write(','.join(record) + '\n')

            another_rent = input("Do you want to rent another land? (y/n): ").strip().lower()
            if another_rent != 'y':
                break
        else:
            print("The land is not available for rent.")
    
    customer_name = input("Enter your name: ")
    return rented_lands, customer_name

def handle_return():
    """
    Handles the process of returning rented land.
    
    Returns:
        tuple: A tuple containing the list of returned lands and the customer's name.
    """
    land_records = load_land_records()
    returned_lands = []

    while True:
        display_land_records()
        land_id = input("Enter the ID of the land you want to return: ")

        if not land_id.isnumeric() or int(land_id) < 1 or int(land_id) > len(land_records):
            print("Invalid ID. Please enter a valid land ID.")
            continue

        idx = int(land_id) - 1

        if land_records[idx][-1].strip() == "Not Available":
            rented_months = input("Enter the number of months the land was rented for: ")

            if not rented_months.isnumeric() or int(rented_months) <= 0:
                print("Invalid input. Please enter a positive number for months.")
                continue

            return_months = input("Enter the number of months the land is being returned after: ")

            if not return_months.isnumeric() or int(return_months) < int(rented_months):
                print("Invalid input. Return months should be greater than or equal to rented months.")
                continue

            total_price = int(land_records[idx][4]) * int(return_months)
            land_records[idx][-1] = "Available"
            returned_lands.append([*land_records[idx][:4], rented_months, return_months, total_price])

            with open('land_data.txt', 'w') as file:
                for record in land_records:
                    file.write(','.join(record) + '\n')

            another_return = input("Do you want to return another land? (y/n): ").strip().lower()
            if another_return != 'y':
                break
        else:
            print("The land is already available for rent.")
    
    customer_name = input("Enter your name: ")
    return returned_lands, customer_name
