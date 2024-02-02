def get_input() -> float:
    # get user input
    user_input = input("Enter your grade percentage as a decimal: ")

    try:
        # convert input to a float that's between 0 and 1
        user_input = float(user_input)
        if user_input < 0 or user_input > 1:
            raise Exception(f"Invalid percentage: \'{user_input}\' => Value between 0 and 1 expected.")

    except ValueError:  # conversion error
        exit(f'Invalid input: \'{user_input}\' => Expected numerical characters')
    except Exception as error:  # percentage out-of-bounds error
        exit(error)

    # validated float between 0 and 1
    return user_input


def calculate_grade(percentage: float) -> None:
    print("Grade: ", end="")
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
    calculate_grade(get_input())


main()
