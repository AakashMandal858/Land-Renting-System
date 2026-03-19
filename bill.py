# bill.py
from datetime import datetime

def generate_rent_bill(rented_lands, customer_name):
    """
    Generate a bill for rented lands.

    Args:
        rented_lands (list): List of rented lands.
        customer_name (str): Name of the customer.

    Returns:
        str: Bill details as a formatted string.
    """
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bill_details = f"Date of Rent: {date}\n"
    bill_details += (
        "Kitta Number".ljust(15) +
        "City".ljust(20) +
        "Land Faced".ljust(20) +
        "Anna".ljust(20) +
        "Duration (Months)".ljust(20) +
        "Total".ljust(20) + "\n"
    )
    total_amount = 0

    for land in rented_lands:
        kitta_number, city, land_faced, anna, months, total_price = land
        bill_details += (
            f"{kitta_number:<15}" +
            f"{city:<20}" +
            f"{land_faced:<20}" +
            f"{anna:<20}" +
            f"{months:<20}" +
            f"{total_price:<20}\n"
        )
        total_amount += total_price

    bill_details += f"Total Amount: {total_amount}\n"
    bill_details += f"Customer Name: {customer_name}\n"

    return bill_details

def generate_return_bill(returned_lands, customer_name):
    """
    Generate a bill for returned lands.

    Args:
        returned_lands (list): List of returned lands.
        customer_name (str): Name of the customer.

    Returns:
        str: Bill details as a formatted string.
    """
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bill_details = f"Date of Return: {date}\n"
    bill_details += (
        "Kitta Number".ljust(15) +
        "City".ljust(20) +
        "Land Faced".ljust(20) +
        "Anna".ljust(20) +
        "Rented (Months)".ljust(20) +
        "Returned (Months)".ljust(20) +
        "Total".ljust(20) + "\n"
    )
    total_amount = 0
    total_fine = 0

    for land in returned_lands:
        kitta_number, city, land_faced, anna, rented_months, return_months, total_price = land
        fine = 0
        if int(return_months) > int(rented_months):
            fine = (int(return_months) - int(rented_months)) * (int(total_price) * 0.10)
            total_fine += fine
        
        bill_details += (
            f"{kitta_number:<15}" +
            f"{city:<20}" +
            f"{land_faced:<20}" +
            f"{anna:<20}" +
            f"{rented_months:<20}" +
            f"{return_months:<20}" +
            f"{total_price + fine:<20}\n"
        )
        total_amount += total_price + fine

    bill_details += f"Total Fine: {total_fine}\n"
    bill_details += f"Total Amount with Fine: {total_amount}\n"
    bill_details += f"Customer Name: {customer_name}\n"

    return bill_details

def save_rent_bill(bill_details, customer_name):
    """
    Save the rent bill details to a text file.

    Args:
        bill_details (str): Bill details.
        customer_name (str): Name of the customer.
    """
    date = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{customer_name}_rent_{date}.txt"
    with open(file_name, 'w') as file:
        file.write(bill_details)

def save_return_bill(bill_details, customer_name):
    """
    Save the return bill details to a text file.

    Args:
        bill_details (str): Bill details.
        customer_name (str): Name of the customer.
    """
    date = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{customer_name}_return_{date}.txt"
    with open(file_name, 'w') as file:
        file.write(bill_details)
