# Starting Out With Python 5th Edition: Chapter 6 - Exercise 12

# Number of months in a year
MONTHS = 12


def main():
    try:
        # Open the file for reading
        infile = open('steps.txt', 'r')

        # Find month using for loop
        for month in range(1, MONTHS+1):
            steps = 0
            days = get_number_of_days_in_month(month)
            average_steps(days, month, steps, infile)

        # Close the file
        infile.close()
    except IOError:
        print(IOError)
    except ValueError:
        print(ValueError)
    except TypeError:
        print(TypeError)
    except SystemError:
        print(SystemError)


# Function returns the number of days in month that isn't a leap year
def get_number_of_days_in_month(month):
    if (month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12):
        return 31
    if (month == 4 or month == 6
       or month == 9 or month == 11):
        return 30
    if month == 2:
        return 28


# Function returns the name of the current month
def get_month_name(month):
    if month == 1:
        return 'January: '
    elif month == 2:
        return 'February: '
    elif month == 3:
        return 'March: '
    elif month == 4:
        return 'April: '
    elif month == 5:
        return 'May: '
    elif month == 6:
        return 'June: '
    elif month == 7:
        return 'July: '
    elif month == 8:
        return 'August: '
    elif month == 9:
        return 'September: '
    elif month == 10:
        return 'October: '
    elif month == 11:
        return 'November: '
    else:
        return 'December: '


# Function calculates average steps per month
def average_steps(days, month, steps, infile):
    for day in range(1, days+1):
        line = infile.readline()
        steps += int(line)
    print(f'{get_month_name(month)}{steps/days:,.2f} Average Steps')


# Call the main function
if __name__ == '__main__':
    main()
