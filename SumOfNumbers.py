def main():
    try:
        # Open numbers.txt for reading
        infile = open('numbers.txt', 'r')

        # Initialize accumulator
        total = 0

        # For each number in infile, add it to accumulator
        for number in infile:
            total += int(number)

        # Print the total
        print(f'{total:.2f}')

        # Close the file
        infile.close()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()