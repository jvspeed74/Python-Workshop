def get_payment() -> None:
    """
    Calculates the pay rate of a user based off of numeric inputs
    """
    while True:
        try:
            # get user input
            pay_rate = float(input("Enter your pay rate: "))
            hours_worked = float(input("Enter the number of hours worked: "))

            # throw exception if user input is negative
            if pay_rate < 0 or hours_worked < 0:
                raise ValueError

        except ValueError:
            # error clause; continues to next iteration
            print("Please enter positive numeric characters")
            continue
        else:
            # regular rate
            if hours_worked <= 40:
                pay = pay_rate * hours_worked
                print(f'Your payment is ${pay}')

            else:
                # overtime rate
                pay = (pay_rate * 40) + ((hours_worked - 40) * (pay_rate * 1.5))
                print(f'Your payment is ${pay}')

            exit()


get_payment()
