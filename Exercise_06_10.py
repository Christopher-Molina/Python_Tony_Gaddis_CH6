# Starting Out With Python 5th Edition: Chapter 6 - Exercise 10

def main():
    try:
        # Create a variable to control the loop
        num_of_players = int(input('How many player records do you want to create? '))

        # Open file for writing
        outfile = open('golf.txt', 'w')
        
        # Add records to the file
        for count in range(1, num_of_players + 1):
            player_name = input('Enter player\'s name: ')
            player_score = input('Enter player\'s score: ')

            # Write the data as a record to the file
            outfile.write(f'Name: {player_name}\nScore: {player_score}\n')

            # Display a blank line
            print()

        # Close the file
        outfile.close()
        print('Player records written to golf.txt')

        # Display records
        print('\nWould you like to see player records?')
        answer = input('Y = yes, anything else = no: ')
        if answer == 'y' or answer == 'Y':
            display_records()
    except IOError:
        print(IOError)
    except TypeError:
        print(TypeError)
    except ValueError:
        print(ValueError)


def display_records():
    # Open the file for reading
    infile = open('golf.txt', 'r')

    # Display the player records
    print('\nRecords:')
    i = 1
    for line in infile:
        if i % 2 == 0:
            print(line.rstrip('\n'))
            print()
            i += 1
        else:
            print(line.rstrip('\n'))
            i += 1

    # Close the file
    infile.close()


# Call the main function
if __name__ == '__main__':
    main()
