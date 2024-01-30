def get_payment():
    while True:
        try:
            pay_rate = float(input("Enter your pay rate: "))
            hours_worked = float(input("Enter the number of hours worked: "))
        except ValueError:
            print("Invalid input")
            continue
        else:
            if hours_worked <= 40:
                pay = pay_rate * hours_worked
                print(f'Your payment is ${pay}')
            else:
                pay = (pay_rate * 40) + ((hours_worked - 40) * (pay_rate * 1.5))
                print(f'Your payment is ${pay}')

            exit()


get_payment()
