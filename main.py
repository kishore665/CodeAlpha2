'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "AMZN": 130,
    "MSFT": 310
}

portfolio = {}
total_value = 0

print("📈 Welcome to the Stock Portfolio Tracker")
print("Available stocks:", ', '.join(stock_prices.keys()))
print("Type 'done' when finished.\n")

# User input loop
while True:
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("❌ Stock not recognized. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print("❌ Invalid number. Try again.")
        continue
    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Calculate total investment
print("\n💼 Portfolio Summary:")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_value += value
    print(f"{stock}: {quantity} shares @ ${price} = ${value}")

print(f"\n🔢 Total Investment Value: ${total_value}")

# Save to file (optional)
save = input("Do you want to save this to a file? (yes/no): ").lower()
if save == 'yes':
    filename = input("Enter filename (e.g., portfolio.txt or portfolio.csv): ")
    with open(filename, 'w') as file:
        file.write("Stock,Quantity,Price,Total Value\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity
            file.write(f"{stock},{quantity},{price},{value}\n")
        file.write(f"\nTotal Investment Value: ${total_value}")
    print(f"📁 Portfolio saved to '{filename}'")


