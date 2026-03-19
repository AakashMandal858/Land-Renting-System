# read.py

def load_land_records(file_name='land_data.txt'):
    """
    Load land records from the given file.

    Args:
        file_name (str): Name of the file containing land records.

    Returns:
        list: List of land records where each record is a list of attributes.
    """
    land_records = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                land_records.append(line.strip().split(','))
    except FileNotFoundError:
        print(f"File {file_name} not found.")
    return land_records

def display_land_records(file_name='land_data.txt'):
    """
    Display land records in a formatted table.

    Args:
        file_name (str): Name of the file containing land records.
    """
    land_records = load_land_records(file_name)
    col_widths = {
        "id": 5,
        "kitta_number": 15,
        "city": 15,
        "land_faced": 18,
        "anna": 15,
        "price": 25,
        "status": 15
    }

    header = (
        "ID".ljust(col_widths["id"]) +
        "Kitta Number".ljust(col_widths["kitta_number"]) +
        "City".ljust(col_widths["city"]) +
        "Land Faced".ljust(col_widths["land_faced"]) +
        "Anna".ljust(col_widths["anna"]) +
        "Price".ljust(col_widths["price"]) +
        "Status".ljust(col_widths["status"])
    )
    print(header)

    for idx, record in enumerate(land_records, start=1):
        if len(record) >= 6:
            kitta_number, city, land_faced, anna, price, status = record[:6]
            row = (
                f"{idx:<{col_widths['id']}}" +
                f"{kitta_number:<{col_widths['kitta_number']}}" +
                f"{city:<{col_widths['city']}}" +
                f"{land_faced:<{col_widths['land_faced']}}" +
                f"{anna:<{col_widths['anna']}}" +
                f"{price:<{col_widths['price']}}" +
                f"{status:<{col_widths['status']}}"
            )
            print(row)
        else:
            print(f"{idx:<{col_widths['id']}} Invalid record format: {record}")
