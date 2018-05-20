import csv

file_name = "data file.csv"

# Catch the exception if the file open fails
try:
    # Try to create a file handle for reading
    file_in = open(file_name, "r")

    # Create a csv object for reading
    csv_in = csv.reader(file_in)

    inventory = []
    # Get each line using the csv object
    for each in csv_in:
        inventory.append(each)

    print(inventory)

    for each in inventory:
        print(each)

    # Close the file when done
    file_in.close()


except FileNotFoundError:
    print(file_name, "not found")
    exit(1)
