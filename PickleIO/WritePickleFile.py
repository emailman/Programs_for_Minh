import pickle

# Define the Bird class
from PickleIO.Bird import Bird


def main():
    birds = []

    # Create a list of Bird objects
    birds.append(Bird("Huey", 13, "Duck"))
    birds.append(Bird("Dewey", 10, "Duck"))
    birds.append(Bird("Louie", 12, "Duck"))
    birds.append(Bird("Jerry", 15, "Goose"))
    birds.append(Bird("Quacky", 7, "Goose"))

    print("Writing these objects:")
    print(birds)
    for each in birds:
        print(each)

    # Open the output file in binary/write mode
    # and close it automatically when done
    with open('birds.pickled', 'wb') as out_file:
        # Pickle the list and write it to the output file
        pickle.dump(birds, out_file)


main()
