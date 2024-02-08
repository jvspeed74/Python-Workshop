"""
Overview of Functions:
- get_mode_type(): Prompts the user to select the mode type (LCM or GCF) and validates the input.
- get_two_int(): Prompts the user to enter two integers, validates the input, and returns them in a sorted list.
- calculate_LCM(a, b): Calculates the Least Common Multiple (LCM) of two integers using the standard formula.
- calculate_GCF(a, b): Calculates the Greatest Common Factor (GCF) of two integers using the Euclidean Algorithm.
- main(): Orchestrates the flow of the program by calling function in order. Contains decorators via print statements.

"""


def get_mode_type() -> str:
    """
    Prompts the user to enter the mode type (LCM or GCF).

    :return: The mode type selected by the user.
    :rtype: str
    """
    while True:
        mode_type = input("Enter 'LCM' or 'GCF': ").upper()

        # check/return if user input is valid
        valid_modes = ['LCM', 'GCF']  # list of acceptable inputs
        if mode_type in valid_modes:
            return mode_type

        print(f"Your input, '{mode_type}', is not in the list of options. Please try again.")
        continue


def get_two_int() -> list[int]:
    """
    Prompts the user to enter two integers, validates the input, and returns them in a sorted list.

    Returned integers follow specific constraints to ensure that calculate_LCM and calculate_GCF are correct:
    - Must be positive.
    - Must be in order of greatest to least.

    :return: A list containing two integers provided by the user.
    :rtype: list[int]
    """
    while True:  # get input 1
        input_one = input("Enter your first integer: ")

        try:
            input_one = int(input_one)
        except ValueError:
            print(f"Invalid input: '{input_one}'. Your input is not a valid integer.")
            continue

        break  # escape loop 1 if valid

    while True:  # get input 2
        input_two = input("Enter your second integer: ")

        try:
            input_two = int(input_two)
        except ValueError:
            print(f"Invalid input: '{input_two}'. Your input is not a valid integer.")
            continue

        break  # escape loop 2 if valid

    # validate negative integers
    input_one, input_two = abs(input_one), abs(input_two)

    # sort numbers greatest to least and return
    return sorted([input_one, input_two], reverse=True)


def calculate_LCM(a: int, b: int) -> int | str:
    """
    Calculates the Least Common Multiple (LCM) of two integers. Arguments must be entered in order from greatest to
    least.

    :param a: The larger integer of the pair.
    :type a: int
    :param b: The smaller integer of the pair.
    :type b: int
    :return: The LCM of the two integers or 'Undefined' if a and b are zero.
    :rtype: int | str
    """
    # base case: LCM between two zeroes does not exist
    if a == 0 and b == 0:
        return "Undefined"

    # base case: If one of the numbers is zero, then the LCM is always zero
    if b == 0:
        return 0

    # convert back to int after conversion equation and return
    return int((a * b) / calculate_GCF(a, b))


def calculate_GCF(a: int, b: int) -> int | str:
    """
    Calculates the Greatest Common Factor (GCF) of two integers using the Euclidean Algorithm. In each recursive
    call, the function passes 'a' and 'b' such that 'b' becomes 'a % b', effectively reducing the problem size
    until 'b' reaches 0, at which point 'a' becomes the GCF.

    :param a: The larger integer of the pair.
    :type a: int
    :param b: The smaller integer of the pair.
    :type b: int
    :return: The GCF of the two integers or 'Undefined' if a and b is zero.
    :rtype: int | str
    """
    # base case: If both numbers are zero, the GCF is undefined because every number is a divisor of zero
    if a == 0 and b == 0:
        return "Undefined"

    # base case: If one of the numbers is zero, the GCF is the other non-zero number
    if b == 0:
        return a

    # recursive call
    return calculate_GCF(b, a % b)


def main():
    """
    Organizes and calls the script functions sequentially. Decorators in the form of print statements are declared with
    the intention of guiding the user throughout the process.

    """
    # welcome decorator
    print("======== LCM/GCF Calculator ========")
    print("*   This program calculates the    *")
    print("* Least Common Multiple (LCM) and  *")
    print("* Greatest Common Factor (GFC) by  *")
    print("* taking two integers from user.   *")

    # infinite loop
    while True:
        # get mode from user
        print("====== Select Calculator Mode ======")
        mode = get_mode_type()

        # get two int from user
        print(f"============ Mode: {mode} =============")
        first_num, second_num = get_two_int()

        # display results based on mode selection
        print(f"============== Result ==============")
        if mode == 'LCM':
            print(f"The LCM for {first_num} and {second_num} is: {calculate_LCM(first_num, second_num)}")
        else:  # GCF
            print(f"The GCF for {first_num} and {second_num} is: {calculate_GCF(first_num, second_num)}")

        # prompt user to end script; break the loop if true else continue
        print(f"============= Continue? ============")
        if input("Enter 'Stop' to exit the script: ").upper() == 'STOP':
            print('Exiting... Goodbye!')
            break


main()
