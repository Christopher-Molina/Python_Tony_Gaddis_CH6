# Starting Out With Python 5th Edition: Chapter 3 - Exercise 4

def main():
    try:
        # Open the file for reading
        infile = open('names.txt', 'r')

        name = infile.readline()  # Priming read
        count = 1  # One name read by priming read
        while name != '':
            count += 1
            name = infile.readline()

        print('The file has ' + str(count) + ' name\\s')

        # Close the file
        infile.close()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
