bodies = []

# The "\n" creates new lines for each record
bodies.append("1 : M : John Doe: 45 : 72 : 180\n")
bodies.append("2 : F : Jane Doe: 40 : 62 : 120\n")

# Create a file handle for output
file_out = open("inventory.txt", "w")

# Write all the lines in the list
file_out.writelines(bodies)

file_out.close()
