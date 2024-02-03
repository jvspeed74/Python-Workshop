# module used to print formatted calendar data
import calendar

# global dictionary mapping month names to their corresponding indices in the calendar module
month_dict = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12,
}


def get_month() -> int:
    """
    Prompts the user to enter a month found in the Gregorian calendar. The program will search for the input
    in month_dict. If the month is not in the calendar, an exception will be raised.

    :return: User input converted to calendar module index.
    :rtype: int
    """
    # Get user input
    input_month = input("Enter a full month name (e.g., January, january, JaNuAry): ").capitalize()

    try:
        # Search for month in dict.
        month_value = month_dict[input_month]

    except KeyError as e:  # month not found in dict
        exit(f"Month name not found: {e} ==> Ensure the use of the Gregorian calendar.")

    # Value successfully extracted from month_dict
    return month_value


def display_calendar(month_value: int) -> None:
    """
    Incorporates the 'calendar' module to display the calendar and day info for the given month.

    :param month_value: An integer between 1 and 12 representing the month values.
    :type month_value: int
    """
    # open wrapper
    print('=' * 30)

    # display full calendar
    print(calendar.month(2023, month_value))

    # display string formatted to show the number of days in the month
    print(f'{calendar.month_name[month_value]} had {calendar.monthrange(2023, month_value)[1]} days in 2023!')

    # closing wrapper
    print('=' * 30)


def main():
    """
    Main function to execute the program. Prints a month from the Gregorian calendar associated with user input.
    """
    display_calendar(get_month())


# Execute the main function
main()
