def find_min_loss(prices):
    n = len(prices)
    min_loss = float('inf')
    buy_year = -1
    sell_year = -1

    for i in range(n):
        for j in range(i + 1, n):
            if prices[j] < prices[i]:
                loss = prices[i] - prices[j]
                if loss < min_loss:
                    min_loss = loss
                    buy_year = i + 1  # year index starts at 1
                    sell_year = j + 1

    if buy_year == -1:
        return "No valid buy/sell to incur a loss."
    else:
        return f"Buy in year {buy_year}, Sell in year {sell_year}, Loss: {min_loss}"


if __name__ == "__main__":
    try:
        num_years = int(input("Enter number of years: "))
        if num_years <= 1:
            print("Need at least 2 years to compute loss.")
        else:
            prices = list(map(int, input(f"Enter {num_years} distinct prices separated by space: ").split()))
            if len(prices) != num_years:
                print("Number of prices doesn't match number of years.")
            elif len(set(prices)) != len(prices):
                print("Prices must be distinct.")
            else:
                result = find_min_loss(prices)
                print("\nResult:")
                print(result)
    except Exception as e:
        print("Error:", e)
