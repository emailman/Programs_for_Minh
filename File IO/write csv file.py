import csv

birds = [[1, "Huey", 13, "Duck"],
         [2, "Dewey", 10, "Duck"],
         [3, "Louie", 12, "Duck"],
         [4, "Jerry", 15, "Goose"],
         [5, "Quacky", 7, "Goose"]]

# Open a text file for write, without a newline character
file_out = open("data file.csv", "w", newline="")

# Create a csv object for writing
csv_out = csv.writer(file_out)

# Write all the rows in list using the csv object
csv_out.writerows(birds)

# Close the file when done
file_out.close()
