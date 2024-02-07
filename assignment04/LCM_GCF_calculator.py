"""
Get mode type from user
Get two integer inputs from user
Calculate either LCM or GCF
Prompt user to stop
"""


def get_mode_type():
    while True:
        mode_type = input("Enter 'LCM', 'GCF', or 'Stop': ").upper()

        mode_options = ['LCM', 'GCF', 'STOP']
        if mode_type in mode_options:
            return mode_type

        print(f"Your input, '{mode_type}', is not in the list of options. Please try again.")
        continue


def get_two_int():
    while True:
        input_one = input("Enter your first integer: ")

        try:
            input_one = int(input_one)
        except ValueError:
            print(f"Invalid input: '{input_one}'. Your input is not an integer.")
            continue

        break  # exit loop 1

    while True:
        input_two = input("Enter your second integer: ")

        try:
            input_two = int(input_two)
        except ValueError:
            print(f"Invalid input: '{input_two}'. Your input is not an integer.")
            continue

        break  # exit loop 2

    # get rid of negative integers
    input_one, input_two = abs(input_one), abs(input_two)
    return sorted([input_one, input_two], reverse=True)


def calculate_LCM(a, b):
    # base cases
    if a == 0 and b == 0:
        return "Undefined"

    if a == 0 or b == 0:
        return 0

    return (a * b) / calculate_GCF(a, b)


def calculate_GCF(a, b):
    # base cases
    if a == 0 and b == 0:
        return "Undefined"

    if b == 0:
        return a

    return calculate_GCF(b, a % b)


def main():
    # welcome statement
    while True:
        mode = get_mode_type()

        if mode == 'STOP':
            print('Exiting program.')
            break

        first_num, second_num = get_two_int()

        if mode == 'LCM':
            pass
        else:  # GCF
            pass


main()

