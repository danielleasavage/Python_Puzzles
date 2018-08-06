import sys

lazy_input = sys.stdin.read().strip().split('\n')
    
lazy_input = [int(x) for x in lazy_input]
lazy_input.pop(0)
input_prices = lazy_input


def check_if_buy(prices):
    if prices[0] < prices[1]:
        return True
    else:
        return False

def check_if_sell(prices):
    if prices[0] > prices[1]:
        return True
    else:
        return False

def determine_how_rich(input_prices):
    money = 100
    coins = 0
    while len(input_prices) > 1:
        if check_if_buy(input_prices)and money >= input_prices[0]:
            coins = int(money/input_prices[0])
            money -= coins * input_prices[0]
            if coins > 100000:
                coins = 100000
            input_prices.pop(0)
        elif check_if_sell(input_prices) and coins != 0:
            money += coins * input_prices[0]
            coins = 0
            input_prices.pop(0)
        else:
            input_prices.pop(0)
    if coins > 0:
        money += coins * input_prices[0]
    return money

print(determine_how_rich(input_prices))