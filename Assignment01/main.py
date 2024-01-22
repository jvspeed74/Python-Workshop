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


def get_dollar_amount(dollars, memo=None):
    if memo is None:
        memo = defaultdict(int)

    for i in range(len(dollar_deno)):
        if dollars - dollar_deno[i] < 0:
            continue

        dollars -= dollar_deno[i]
        memo[dollar_deno[i]] += 1
        return get_dollar_amount(dollars, memo)

    for k, v in memo.items():
        print(f"${k} bills required: {v}")


def get_coin_amount(coins, memo=None):
    if memo is None:
        memo = defaultdict(int)

    for i in range(len(coin_deno)):
        if coins - coin_deno[i] < 0:
            continue

        coins -= coin_deno[i]
        memo[coin_deno[i]] += 1
        return get_coin_amount(coins, memo)

    for k, v in memo.items():
        print(f"{k}¢ required: {v}")


def get_answer(dollar_dict, coin_dict):
    for k, v in dollar_dict.items():
        print(f"${k} bills required: {v}")

    for k, v in coin_dict.items():
        print(f"{k}¢ cents required: {v}")


def main():
    for tender, cost in tender_cost.items():
        print(f"Tender: ${tender}, Cost: ${cost}")
        change = get_change(tender, cost)
        print(f"Your change is $"'{:.2f}'.format(change))
        dollars, coins = str(change).split(".")
        get_dollar_amount(int(dollars))
        get_coin_amount(int(coins))
        print("============================")


main()
