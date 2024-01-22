from collections import defaultdict

# declare denominations
dollar_deno = [100, 50, 20, 10, 5, 1]
coin_deno = [25, 10, 5, 1]

# declare test cases:
# {key: value} == {amount_tendered: item_cost}
tender_cost = {
    100: 36.57,
    80: 64.09,
    10: 3.81,
    50: 14.36
}


def get_change(tender, cost):
    """
    Calculates the difference between tender and cost
    :param float tender:
    :param float cost:
    :return: tender minus cost rounded to two decimal places
    :rtype: float
    """
    return round(tender - cost, 2)


def get_minimum_amount(value, deno, memo=None):
    """
    Finds the minimum amount of the set denomination required to reach zero using recursion
    :param int value: Remaining change to find the minimum amount for
    :param list deno: List of the denominations to use for recursion
    :param dict memo: Memoization dictionary used to store results
    :return: Dictionary with the count of each required denomination
    :rtype: dict
    """

    # declare dict for memoization
    if memo is None:
        memo = defaultdict(int)

    if value == 0:
        return memo

    # iterate through denominations
    for i in range(len(deno)):
        if value - deno[i] < 0:
            continue

        value -= deno[i]
        memo[deno[i]] += 1
        return get_minimum_amount(value, deno[i:], memo)

    return memo


def get_answer(dollar_dict, coin_dict):
    """
    Formats and prints the minimum amount of dollars and coins
    :param dict dollar_dict: Dictionary containing required dollar information
    :param dict coin_dict: Dictionary containing required coin information
    """
    for k, v in dollar_dict.items():
        print(f"${k} bills required: {v}")

    for k, v in coin_dict.items():
        print(f"{k}¢ required: {v}")


def main():
    """
    Iterates through test cases and prints the minimum amount of dollars and coins required.
    """
    # iterate through each item in the test case
    for tender, cost in tender_cost.items():
        # print test case
        print(f"Tender: ${tender}, Cost: ${cost}")

        # calculate and print change
        change = get_change(tender, cost)
        print(f"Your change is ${change}")

        # because of floating-point inaccuracies, split dollars and coins into separate integers
        dollars, coins = str(change).split(".")
        dollars, coins = int(dollars), int(coins)

        # pass dollars, coins into recursive function get_minimum_amount which returns dict
        # pass dict into get_answer to print answers in appropriate format
        get_answer(get_minimum_amount(dollars, dollar_deno), get_minimum_amount(coins, coin_deno))

        # decorator between iterations
        print("============================")


main()
