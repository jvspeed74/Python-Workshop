def get_percentage() -> float:
    """
    Prompts the user to enter a decimal between 0 and 1. The program will validate and return the
    input as a float.
    :return: User input as a float.
    :rtype: float
    """
    # get user input
    user_input = input("Enter your grade percentage as a decimal: ")

    try:
        # convert input to a float that's between 0 and 1
        user_input = float(user_input)
        if user_input < 0 or user_input > 1:
            raise Exception(f"Invalid percentage: \'{user_input}\' => Value between 0 and 1 expected.")

    except ValueError:  # conversion error
        exit(f'Invalid input: \'{user_input}\' => Expected input consisting of only number and decimal characters.')
    except Exception as error:  # percentage out-of-bounds error
        exit(error)

    # validated float between 0 and 1
    return user_input


def calculate_letter_grade(percentage: float) -> None:
    """
    Prints the overall letter grade based from percentage conditional.
    :param percentage: Numerical input between 0 and 1 representing the grade percentage.
    :type percentage: float
    """
    # formatter
    print("Grade: ", end="")

    # find numerical band that percentage resides in
    if percentage >= 0.97:
        print("A+")
    elif percentage >= 0.93:
        print("A")
    elif percentage >= 0.9:
        print("A-")
    elif percentage >= 0.87:
        print("B+")
    elif percentage >= 0.83:
        print("B")
    elif percentage >= 0.8:
        print("B-")
    elif percentage >= 0.77:
        print("C+")
    elif percentage >= 0.73:
        print("C")
    elif percentage >= 0.7:
        print("C-")
    elif percentage >= 0.67:
        print("D+")
    elif percentage >= 0.63:
        print("D")
    elif percentage >= 0.6:
        print("D-")
    else:
        print("F")


def main():
    """
    Main function to execute the program. Calculates and prints the letter grade based on the user's input percentage.
    """
    calculate_letter_grade(get_percentage())


main()
