# Create a file handle for reading the text file
file_in = open("inventory.txt", "r")

# Read all the lines in the file
bodies = file_in.readlines()

print(bodies)

# Remove the new line character on each line
bodies = [each.strip("\n") for each in bodies]

print(bodies)

for each in bodies:
    print(each)
