def get_point():
    # get user input
    x_input = input("Enter an x-coordinate: ")
    y_input = input("Enter an y-coordinate: ")

    try:
        # convert to int
        x_input = int(x_input)
        y_input = int(y_input)
    except ValueError:
        exit("Please enter an integer")
    else:
        return x_input, y_input


def find_quadrant(x, y):
    if x > 0:
        if y > 0:
            return "I"
        else:
            return "IV"
    else:
        if y > 0:
            return "II"
        else:
            return "III"


def main():
    x, y = get_point()
    print(find_quadrant(x, y))


main()
