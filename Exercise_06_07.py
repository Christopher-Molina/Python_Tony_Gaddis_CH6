# Starting Out With Python 5th Edition: Chapter 6 - Exercise 7

import random


def main():
    try:
        # Open file for writing
        outfile = open('Random.txt', 'w')

        # For each count in range, write random number to outfile
        for count in range(int(input('How many numbers will the file hold? '))):
            line = str(random.randint(1, 500))
            outfile.write(f'{line}' + '\n')

        # Close the file
        outfile.close()
        print('The numbers have been added to Random.txt.')
    except IOError:
        print(IOError)
    except TypeError:
        print(TypeError)
    except ValueError:
        print(ValueError)


if __name__ == '__main__':
    main()
