MAX = 5


def main():
    try:
        # Input name of the file
        filename = input('Enter a filename: ')

        # Open the file for reading
        infile = open(filename, 'r')

        # Priming read
        line = infile.readline()
        lines_read = 1

        # If the file contains more than max lines, print only 5
        while line != '' and lines_read <= MAX:
            print(line.rstrip('\n'))  # Print the current line without \n
            line = infile.readline()  # Read the next line
            lines_read += 1  # Increase lines read by 1 each iteration

        # Close the file
        infile.close()
    except Exception as e:
        print(e)


# Call the main function
if __name__ == '__main__':
    main()
