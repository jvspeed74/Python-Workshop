"""
Name: Jalen Vaughn
Date: 2/13/24
File: infinite_sums.py
Description: Uses Madhava-Leibniz series
Dependencies/Imports: 
"""


def get_input() -> int:
    """
    Gets user input and type casts it to int.
    :return: A positive integer
    :rtype: int
    """
    while True:
        user_input = input("Enter an integer: ")

        try:
            user_input = int(user_input)

        except ValueError:
            print("Invalid number")
            continue

        return abs(user_input)


def infinite_sums(n: int) -> float:
    """
    Calculates the infinite sum of the Medhava-Leibniz series.
    :param n: An integer used as a range() stopping point.
    :type n: int
    :return: The result of the infinite sum equation.
    :rtype: float
    """
    sum_Terms = 0
    for i in range(0, n + 1):
        sum_Terms += ((-1) ** i) * 4 / (2 * i + 1)

    return sum_Terms


def main():
    """
    This program calculates the infinite sum of the Medhava-Leibniz series. The user can input a positive
    integer that will serve as a stopping point for the series. The result of the calculation is then displayed in the
    terminal.
    """
    n = get_input()
    ans = infinite_sums(n)
    print(ans)


main()
