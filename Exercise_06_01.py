# Starting Out With Python 5th Edition: Chapter 6 - Exercise 1

def main():
    try:
        # Open the file for reading
        infile = open('numbers.txt', 'r')

        # For each line in infile, print the line
        for line in infile:
            print(line)

        # Close the file
        infile.close()
    except Exception as e:
        print(e)


# Call the main function
if __name__ == '__main__':
    main()
