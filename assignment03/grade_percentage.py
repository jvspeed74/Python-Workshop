def get_input() -> float:
    try:
        user_input = float(input("Enter your grade percentage as a decimal: "))

        if user_input < 0 or user_input > 1:
            raise Exception(f"Invalid percentage: \'{user_input}\' => Value between 0 and 1 expected.")

    except Exception as error:
        print(error)

    else:
        return user_input


get_input()
