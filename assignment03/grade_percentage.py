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


get_input()
