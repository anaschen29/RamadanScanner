import os
from datetime import datetime

def create_taps_file():
    # Get the current date and time
    current_datetime = datetime.now()
    date_str = current_datetime.strftime("%m-%d")

    # Construct the filename
    filename = os.path.join("taps", f"taps({date_str}).txt")

    # Create an empty file
    with open(filename, 'w'):
        pass

    print(f"Empty file '{filename}' created.")

if __name__ == "__main__":
    create_taps_file()