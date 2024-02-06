def get_int():
    user_input = input("Please enter an integer: ")
    try:
        user_input = int(user_input)
    except ValueError:
        exit("Invalid input")

    if user_input < 0:
        exit("Enter a positive integer")

    return user_input


def hailstone_number_generator(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:

            n *= 3
            n += 1

        count += 1

        if count == 20 or n == 1:
            break

    return count


def main():
    print(hailstone_number_generator(get_int()))


main()
