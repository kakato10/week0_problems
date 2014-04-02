def calculate_coins(sum):

    coins = {1: 0, 2: 0, 5: 0, 10: 0, 20: 0, 50: 0, 100: 0}
    list_of_coins = [100, 50, 20, 10, 5, 2, 1]
    sum = round(sum * 100)
    for i in list_of_coins:
        while i <= sum:
            coins[i] = coins[i] + 1
            sum = sum - i

    return coins
