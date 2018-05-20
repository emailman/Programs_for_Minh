import pickle
# Note we don't have to import the Bird class


def main():

    # Open the file for reading in binary mode
    # The file will be automatically closed when done
    with open('birds.pickled', 'rb') as in_file:
        # Create a list by loading the file using pickle
        birds = pickle.load(in_file)

    print("These object were read from a file:")
    print(birds)
    for each in birds:
        print(each)


main()
