def main():
    try:
        # Open the file for reading
        infile = open('Random.txt', 'r')

        # Initialize accumulator variables
        total = 0
        lines_read = 0

        # For each line read in infile, add line to total and increment lines read.
        for line in infile:
            total += int(line)  # Convert to int and add to total
            lines_read += 1  # Increment lines read per iteration
            print(line.rstrip('\n'))

        # Display the total of the numbers and lines read
        print(f'\nSum: {total:,.0f}\nNumbers: {lines_read}')

        # Close the file
        infile.close()
    except IOError:
        print(IOError)
    except TypeError:
        print(TypeError)
    except ValueError:
        print(ValueError)


if __name__ == '__main__':
    main()
