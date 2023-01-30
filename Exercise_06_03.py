# Starting Out With Python 5th Edition: Chapter 6 - Exercise 3

def main():
    try:
        # Input the name of a file
        filename = input('Enter a filename: ')

        # Open the file
        infile = open(filename, 'r')

        # For each line in infile, display each line
        # with line number preceded by a colon
        line_numbering = 1
        for line in infile:
            print(str(line_numbering) + ': ' + line.rstrip('\n'))
            line_numbering += 1

        # Close the file
        infile.close()
    except Exception as e:
        print(e)


# Call the main function
if __name__ == '__main__':
    main()
