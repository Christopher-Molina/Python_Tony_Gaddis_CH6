# Starting Out With Python 5th Edition: Chapter 6 - Exercise 6

def main():
    try:
        # Open the file for reading
        infile = open('numbers.txt', 'r')

        # Initialize accumulator
        total = 0.0
        lines_read = 1

        for line in infile:
            total += float(line)
            lines_read += 1
        print(f'Average of numbers is {total / lines_read:.2f}')
    except IOError:
        print(IOError)
    except ValueError:
        print(ValueError)


# Call the main function
if __name__ == '__main__':
    main()
