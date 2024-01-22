from collections import defaultdict

# Find change
# Find dollar amount
# Find coin amount
# Use recursion to subtract the highest dollar/coin value and store values in dict

# declare denominations
dollar_deno = [100, 50, 20, 10, 5, 1]
coin_deno = [25, 10, 5, 1]

# declare test cases
tender_cost = {
    100:36.57,
    80:64.09,
    10:3.81,
    50:14.36
}


def get_change(tender, cost):
    return round(tender - cost, 2)


def get_minimum_amount(value, deno, memo=None):
    if memo is None:
        memo = defaultdict(int)

    for i in range(len(deno)):
        if value - deno[i] < 0:
            continue

        value -= deno[i]
        memo[deno[i]] += 1
        return get_minimum_amount(value, deno, memo)

    return memo


def get_answer(dollar_dict, coin_dict):
    for k, v in dollar_dict.items():
        print(f"${k} bills required: {v}")

    for k, v in coin_dict.items():
        print(f"{k}¢ required: {v}")


def main():
    for tender, cost in tender_cost.items():
        print(f"Tender: ${tender}, Cost: ${cost}")
        change = get_change(tender, cost)
        print(f"Your change is ${change}")
        dollars, coins = str(change).split(".")
        dollars, coins = int(dollars), int(coins)
        get_answer(get_minimum_amount(dollars, dollar_deno), get_minimum_amount(coins, coin_deno))
        print("============================")


main()
