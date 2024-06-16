# Best Time to Buy and Sell Stock (leetcode)

from typing import List

def stock(prices: List[int]) -> int:
    if not prices:
        return 0
    
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    
    return max_profit

# Test case
prices = [7, 1, 5, 3, 6, 4, 8]

if __name__ == '__main__':
    print(stock(prices))  # Output should be 5
