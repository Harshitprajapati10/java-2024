# Best time to buy or sell a stock
# Two pointer, 121

def maxProfit(prices):
    l = 0
    r = 0
    profit = 0
    while(r<len(prices)):
        if prices[l] > prices[r]:
            l = r
        else:
            profit = max(profit, prices[r]-prices[l])
        r += 1
    return profit

def main():
    list = [7,1,2,3,6,5]
    print(maxProfit(list))

if __name__ == "__main__":
    main()