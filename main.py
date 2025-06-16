

def max_profit(prices):
    max_profit = 0

    for i in range(1, len(prices)):
        curr = prices[i]
        prev = prices[i - 1]

        if curr > prev:
            max_profit += curr - prev

    return max_profit
